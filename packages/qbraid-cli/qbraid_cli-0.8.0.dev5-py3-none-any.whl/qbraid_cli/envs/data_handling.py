# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module for handling data related to qBraid environments.

"""

import json
import keyword
import re
from pathlib import Path
from typing import Dict, List, Tuple

import typer

from qbraid_cli.handlers import QbraidException


def is_valid_env_name(env_name: str) -> bool:  # pylint: disable=too-many-return-statements
    """
    Validates a Python virtual environment name against best practices.

    This function checks if the given environment name is valid based on certain
    criteria, including length, use of special characters, reserved names, and
    operating system-specific restrictions.

    Args:
        env_name (str): The name of the Python virtual environment to validate.

    Returns:
        bool: True if the name is valid, False otherwise.

    Raises:
        ValueError: If the environment name is not a string or is empty.
    """
    # Basic checks for empty names or purely whitespace names
    if not env_name or env_name.isspace():
        return False

    # Check for invalid characters, including shell metacharacters and spaces
    if re.search(r'[<>:"/\\|?*\s&;()$[\]#~!{}]', env_name):
        return False

    if env_name.startswith("tmp"):
        return False

    # Reserved names for Windows (example list, can be expanded)
    reserved_names = [
        "CON",
        "PRN",
        "AUX",
        "NUL",
        "COM1",
        "COM2",
        "COM3",
        "COM4",
        "COM5",
        "COM6",
        "COM7",
        "COM8",
        "COM9",
        "LPT1",
        "LPT2",
        "LPT3",
        "LPT4",
        "LPT5",
        "LPT6",
        "LPT7",
        "LPT8",
        "LPT9",
    ]
    if env_name.upper() in reserved_names:
        return False

    if len(env_name) > 20:
        return False

    # Check against Python reserved words
    if keyword.iskeyword(env_name):
        return False

    # Check if it starts with a number, which is not a good practice
    if env_name[0].isdigit():
        return False

    return True


def validate_env_name(value: str) -> str:
    """Validate environment name."""
    if not is_valid_env_name(value):
        raise typer.BadParameter(
            f"Invalid environment name '{value}'. " "Please use a valid Python environment name."
        )
    return value


def installed_envs_data() -> Tuple[Dict[str, Path], Dict[str, str]]:
    """Gather paths and aliases for all installed qBraid environments."""
    from qbraid_core.services.environments.paths import get_default_envs_paths, is_valid_slug

    installed = {}
    aliases = {}

    qbraid_env_paths: List[Path] = get_default_envs_paths()

    for env_path in qbraid_env_paths:
        for entry in env_path.iterdir():
            if entry.is_dir() and is_valid_slug(entry.name):
                installed[entry.name] = entry

                if entry.name == "qbraid_000000":
                    aliases["default"] = entry.name
                    continue

                state_json_path = entry / "state.json"
                if state_json_path.exists():
                    try:
                        with open(state_json_path, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        aliases[data.get("name", entry.name[:-7])] = entry.name
                    # pylint: disable-next=broad-exception-caught
                    except (json.JSONDecodeError, Exception):
                        aliases[entry.name[:-7]] = entry.name
                else:
                    aliases[entry.name[:-7]] = entry.name
    return installed, aliases


def request_delete_env(slug: str) -> str:
    """Send request to delete environment given slug."""
    from qbraid_core import QbraidSession, RequestsApiError

    session = QbraidSession()

    try:
        session.delete(f"/environments/{slug}")
    except RequestsApiError as err:
        raise QbraidException("Delete environment request failed") from err
