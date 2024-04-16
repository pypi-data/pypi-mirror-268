import argparse
import yaml
import itertools
import os
import numpy as np
import pandas as pd
from user_utils import safe_eval
from typing import Tuple, List, Optional
from collections import defaultdict, deque

slurm_template = "{HEADER}\n{SETUP}\n{COMMAND}\n{TEARDOWN}\n"
user_readable_dependencies_to_slurm = {"all": "afterok", "forEach": "aftercorr"}


def build_slurm_args_from_uservars(
    user_args: dict,
    num_jobs: int,
    experiment_name: str = "experiment",
    dependencies: Optional[list] = None,
    dependency_types: Optional[list] = None,
) -> str:
    """
    Build the first part of an sbatch script given user specifications (e.g. number of gpus, memory, etc)
    Does not include the array arguments, which are built separately based on depdenencies.
    # TODO: extract the array things later, just adding them here now
    Args:
        user_args (dict): User arguments. Should be named exactly the same as slurm arguments.

    Returns:
        str: String containing the slurm arguments. To be used as a header for an array job.
    """
    slurm_args = "#/bin/bash\n"
    user_slurm_config = user_args.get("slurm")

    default_vars = {
        "job-name": experiment_name,
        "output": "./slurm_logs/%x-%j-%a.out",
        "time": "1-00:00:00",
        "mem": "32G",
        "partition": "general",
    }

    merged_vars = {**default_vars, **user_slurm_config}

    for key, value in merged_vars.items():
        # TODO: maybe add some validation here
        slurm_args += f"#SBATCH --{key}={value}\n"

    # add dependencies
    if dependencies:
        assert len(dependencies) == len(
            dependency_types
        ), "Number of dependencies must match number of dependency types"
        dependency_types = [
            user_readable_dependencies_to_slurm[dep] for dep in dependency_types
        ]
        for dep, dep_type in zip(dependencies, dependency_types):
            slurm_args += f"#SBATCH --depend={dep_type}:{dep}\n"

    if num_jobs > 1:
        concurrent_jobs = user_args.get("concurrent_jobs", 8)
        slurm_args += f"#SBATCH --array=1-{num_jobs}%{concurrent_jobs}\n"

    return slurm_args


def build_setup(
    exp_config: dict, col_headers: list, exp_file_path: str, add_job_info: bool = True
) -> str:
    """
    Build the setup part of the slurm script. This part is responsible for setting up the environment before running the command.
    Note on env setup: this is done after reading in variables, so you can reference any existing variables in your setup commands, such as
    defining variables like "output_file=${model_name}_${learning_rate}_${batch_size}.csv", or doing any other computations your main script needs

    Args:
        exp_config (dict): Setup configuration dictionary. Contains the setup commands to run before the main command.

    Returns:
        str: String containing the setup commands.
    """
    setup_str = ""
    if exp_file_path:
        setup_str += f"config_file={exp_file_path}\n"
        for i, header in enumerate(
            col_headers[1:], start=2
        ):  # awk columns start at 1, read in exp vars in order
            setup_str += f"{header}=$(awk -v TaskID=$SLURM_ARRAY_TASK_ID 'NR==TaskID+1 {{print ${i}}}' $config_file)\n"

    if "setup" in exp_config:
        for line in exp_config["setup"].split("\n"):
            if (
                line[0] == "!"
            ):  # marks a setup utility, right now I have only loading conda envs since I always do that
                setup_str += safe_eval(line, user_vars)
            else:
                setup_str += f"{line}\n"

    if add_job_info:
        setup_str += f"echo '=== JOB INFO ==='\n"
        setup_str += f"echo 'Job ID: $SLURM_JOB_ID'\n"
        setup_str += f"echo 'Array ID: $SLURM_ARRAY_JOB_ID'\n"
        setup_str += f"echo 'Running on: $HOSTNAME'\n"
        # TODO: usually have a list of all variables here but didn't pass them
        setup_str += f"echo '=== END JOB INFO ==='\n"

    return setup_str


def parse_range(range_str: str) -> list:
    """
    Parse a range string into a list of integers.
    The range string should be in the format "start:end:step" or "start:end"

    Args:
        range_str (str): Range string to parse.

    Returns:
        list: List of integers.
    """
    parts = range_str.split(":")
    if len(parts) > 3 or len(parts) < 2:
        raise ValueError(
            f"Invalid range string: {range_str}. Valid range strings are formatted start:end or start:end:step"
        )

    start, end, step = map(float, parts)
    return list(np.arange(start, end, step))


def find_components(experiment_config: dict):
    """Identify all separate components in the graph. Also return entry points (nodes with no dependencies)"""
    visited = set()
    components = []

    def dfs(node, component):
        to_visit = [node]
        while to_visit:
            current = to_visit.pop()
            if current not in component:
                component.add(current)
                to_visit.extend(experiment_config[current].get("dependencies", []))
                to_visit.extend(
                    [
                        n
                        for n, props in experiment_config.items()
                        if current in props.get("dependencies", [])
                    ]
                )

    for node in experiment_config:
        if node not in visited:
            component = set()
            dfs(node, component)
            components.append(component)
            visited.update(component)

    entry_points = [
        node
        for node in experiment_config
        if not experiment_config[node].get("dependencies")
    ]

    assert (
        len(entry_points) > 0
    ), "No entry points found in the experiment configuration"

    return components, entry_points


def topsort(experiment_config: dict, node: dict, seen: set = set()):
    "topsort for use with build_dependency_graph"
    sorted_order = []

    def dfs(node):
        seen.add(node)
        for dep in experiment_config[node].get("dependencies", []):
            if dep not in seen:
                dfs(dep)
        sorted_order.append(node)
        print(node)

    for node in experiment_config:
        if node not in seen:
            dfs(node)

    return sorted_order


def build_dependency_graph(experiment_config: dict) -> dict:
    """
    Build a dependency graph based on the experiment configuration.
    The graph is a dictionary where the key is the experiment id and the value is a list of experiment ids that must be completed before the key experiment can run.

    Args:
        experiment_config (dict): Experiment configuration dictionary.

    Returns:
        dict: Dependency graph.
    """
    # Lol, realized we don't actually need this since the user already has to specify deps,
    # which are managed by slurm. But can use this for visual representation for the user,
    # or to check for cycles, etc.

    if len(experiment_config.keys()) == 1:
        return {list(experiment_config.keys())[0]: list(experiment_config.keys())}

    try:
        connected_components, entry_pts = find_components(experiment_config)
        components = {}
        for connected_component in connected_components:
            entry_pts_of_component = [
                entry_point_name
                for entry_point_name in entry_pts
                if entry_point_name in connected_component
            ]
            seen = set()
            subgraph = {
                k: v for k, v in experiment_config.items() if k in connected_component
            }
            components[tuple(entry_pts_of_component)] = topsort(
                subgraph, entry_pts_of_component[0], seen
            )
    except:
        raise ValueError(
            "Could not build dependency graph. Please check that the dependencies are correctly specified and there are no cycles."
        )

    return components


def generate_experiment_file_for_step(
    experiment_name: str,
    variables: dict,
    command_template: str,
    experiment_type: str = "cartesian",
) -> Tuple[str, List[str], int]:
    """
    Generate an experiment file (csv) for a given step. The experiment file will be read by the slurm array job to run the experiments.
    Each column will be a variable in that step and each row will be a separate experiment, labeled by the experiment id (by default the integers 1-N).
    The experiment file will be saved under ./slurm_jobs/experiment_files/step_{step_id}.csv

    Args:
        variables (dict): Variables for the given step. Each key is a variable name and the value is a list of values to test.
        command_template (str): Command template for the experiment. The command template should contain placeholders for the variables, e.g. {var1}, {var2}, etc.
        experiment_type (str): Type of experiment. Currently cartesian product, sequential (same index for each variable), or random (randomly sample from the values) are supported
    Returns:
        None
    """
    for var_name, var_values in variables.items():
        if isinstance(var_values, str) and ":" in var_values:
            variables[var_name] = parse_range(var_values)

    output_dir = "./slurm_jobs/experiment_files/"
    os.makedirs(output_dir, exist_ok=True)

    if experiment_type == "cartesian":
        # TODO: currently, we rely on the user specifying the variables (for instance in dependencies_simple.yaml train/eval) in the same order.
        # should sort them all by key in the future (unless it's very important exps happen in a certain order? hm)
        combinations = list(itertools.product(*variables.values()))
    elif experiment_type == "sequential":
        assert all(
            len(var_values) == len(variables.values()[0])
            for var_values in variables.values()
        ), "All variables must have the same number of values for sequential experiments"
        combinations = list(zip(*variables.values()))
    elif experiment_type == "random":
        raise NotImplementedError("Random experiments not yet implemented")

    csv_file_path = os.path.join(output_dir, f"{experiment_name}.csv")
    df = pd.DataFrame(combinations, columns=variables.keys())
    df["TaskID"] = df.index + 1
    # reorder to have TaskID as the first column
    df = df[["TaskID"] + list(variables.keys())]

    df["command"] = df.apply(lambda x: command_template.format(**x), axis=1)
    df.to_csv(csv_file_path, index=False)

    return csv_file_path, list(df.columns), len(df)


def generate_slurm_script_for_step(
    user_args: dict,
    experiment_name: str,
    experiment_config: dict,
    experiment_filepath: str,
    num_experiments: int,
    var_headers: List[str],
    dependencies: Optional[List[str]] = None,
    dependency_types: Optional[List[str]] = None,
) -> None:
    # generate header
    header = build_slurm_args_from_uservars(
        user_args, num_experiments, experiment_name, dependencies, dependency_types
    )

    # generate setup
    setup = build_setup(experiment_config, var_headers, experiment_filepath)

    # teardown
    teardown = experiment_config.get("teardown", "")

    slurm_script = slurm_template.format(
        HEADER=header,
        SETUP=setup,
        COMMAND=experiment_config["command"],
        TEARDOWN=teardown,
    )

    with open(f"./slurm_jobs/{experiment_name}.sh", "w") as file:
        file.write(slurm_script)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate commands for experiment automation. This is a meta-script that generates experiment files and slurm scripts given "
    )
    parser.add_argument(
        "experiment_file", type=str, help="Path to the experiment automation YAML file."
    )
    parser.add_argument(
        "--user_vars",
        type=str,
        help="Path to personal user variables for slurm, in yaml format. See the template for the format.",
    )

    # Parse arguments
    args = parser.parse_args()

    # Load the base experiment automation YAML
    with open(args.experiment_file, "r") as file:
        experiment_config = yaml.safe_load(file)

    # Load the user variables
    if args.user_vars:
        with open(args.user_vars, "r") as file:
            user_vars = yaml.safe_load(file)
    else:
        user_vars = {}

    dep_order = build_dependency_graph(experiment_config)

    for entry_points, steps in dep_order.items():
        for step in steps:
            curr_step_config = experiment_config[step]

            variables_for_step = curr_step_config.get("variables", {})
            if len(variables_for_step) > 0:
                step_csv_path, var_headers, num_exps = (
                    generate_experiment_file_for_step(
                        step, curr_step_config["variables"], curr_step_config["command"]
                    )
                )
            else:
                step_csv_path, var_headers, num_exps = "", [], 1

            generate_slurm_script_for_step(
                user_vars,
                step,
                curr_step_config,
                step_csv_path,
                num_exps,
                var_headers,
                dependencies=curr_step_config.get("dependencies", None),
                dependency_types=curr_step_config.get("dependency_type", None),
            )

    print(
        f"Done generating experiment files! Check out the slurm_jobs directory for the files and double check that you want to run all of them."
    )
    print(
        f"Found {len(dep_order)} connected components in the experiment configuration."
    )
    print(f"Entry points: {list(dep_order.keys())}")
