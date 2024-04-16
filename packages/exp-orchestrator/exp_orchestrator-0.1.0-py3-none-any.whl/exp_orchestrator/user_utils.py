# Contains utils that you can use in the "setup" portion of a job.
# To call them, simply add a "!" before the function call, such as !load_env(venv).
# You can also write regular bash code in the setup portion, which will be executed as is.
# Please separate lines with \n of course though
from typing import List


def safe_eval(call_str: str, user_vars: dict) -> str:
    if not call_str.startswith("!"):
        raise ValueError("Setup utilities must start with '!'")

    call_body = call_str[1:]
    if "(" in call_body:
        utility_name, args_str = call_body.split("(", 1)
        utility_name = utility_name.strip()
        args_str = args_str.rstrip(")")
        args = [arg.strip() for arg in args_str.split(",")]
    else:
        utility_name = call_body.strip()
        args = []

    user_utils_registry = {
        "load_env": _load_env,
        "load_lst_from_file": _load_lst_from_file,
    }

    utility_fn = user_utils_registry.get(utility_name)
    if utility_fn is None:
        raise ValueError(
            f"Unknown utility function: {utility_name}. Current utilities: {list(user_utils_registry.keys())}"
        )

    return utility_fn(*args, user_vars=user_vars)


def _load_env(env_name: str, user_vars: dict) -> str:
    """
    Load a conda environment.
    Args:
        env_name (str): Name of the conda environment to load.
        user_vars (dict): Dictionary containing user variables.
    Returns:
        str: String containing the command to load the conda environment.
    """
    conda_loc = user_vars.get("conda_location")
    return f"source {conda_loc}\nconda activate {env_name}\n"


def _load_lst_from_file(filepath: str) -> List[str]:
    """Load a list of variables from a file rather than through direct specification.
    Useful for long lists of string variables. Should be one per line.

    Args:
        filepath (str): Path to the file containing the list of variables.

    Returns:
        list[str]: List of variables.
    """
    with open(filepath, "r") as f:
        return [line.strip() for line in f.readlines()]
