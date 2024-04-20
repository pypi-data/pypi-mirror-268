# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module supporting 'qbraid envs create' command.

"""

import json
import os
import shutil
import subprocess
import sys
from typing import Optional


def replace_str(target: str, replacement: str, file_path: str) -> None:
    """Replace all instances of string in file"""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    content = content.replace(target, replacement)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def update_state_json(
    slug_path: str,
    install_complete: int,
    install_success: int,
    message: Optional[str] = None,
    env_name: Optional[str] = None,
) -> None:
    """Update environment's install status values in a JSON file.
    Truth table values: 0 = False, 1 = True, -1 = Unknown
    """
    # Set default message if none provided
    message = "" if message is None else message.replace("\n", " ")

    # File path for state.json
    state_json_path = os.path.join(slug_path, "state.json")

    # Read existing data or use default structure
    if os.path.exists(state_json_path):
        with open(state_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"install": {}}

    # Update the data
    data["install"]["complete"] = install_complete
    data["install"]["success"] = install_success
    data["install"]["message"] = message

    if env_name is not None:
        data["name"] = env_name

    # Write updated data back to state.json
    with open(state_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def create_venv(slug_path: str, prompt: str) -> None:
    """Create virtual environment and swap PS1 display name."""
    venv_path = os.path.join(slug_path, "pyenv")
    subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)

    # Determine the correct directory for activation scripts based on the operating system
    if sys.platform == "win32":
        scripts_path = os.path.join(venv_path, "Scripts")
        activate_files = ["activate.bat", "Activate.ps1"]
    else:
        scripts_path = os.path.join(venv_path, "bin")
        activate_files = ["activate", "activate.csh", "activate.fish"]

    for file in activate_files:
        file_path = os.path.join(scripts_path, file)
        if os.path.isfile(file_path):
            replace_str("(pyenv)", f"({prompt})", file_path)

    replace_str(
        "include-system-site-packages = false",
        "include-system-site-packages = true",
        os.path.join(venv_path, "pyvenv.cfg"),
    )

    update_state_json(slug_path, 1, 1)


def create_qbraid_env_assets(slug: str, alias: str, kernel_name: str, slug_path: str) -> None:
    """Create a qBraid environment including python venv, PS1 configs,
    kernel resource files, and qBraid state.json."""
    # pylint: disable-next=import-outside-toplevel
    from jupyter_client.kernelspec import KernelSpecManager

    local_resource_dir = os.path.join(slug_path, "kernels", f"python3_{slug}")
    os.makedirs(local_resource_dir, exist_ok=True)

    # create state.json
    update_state_json(slug_path, 0, 0, env_name=alias)

    # create kernel.json
    kernel_json_path = os.path.join(local_resource_dir, "kernel.json")
    kernel_spec_manager = KernelSpecManager()
    kernelspec_dict = kernel_spec_manager.get_all_specs()
    kernel_data = kernelspec_dict["python3"]["spec"]
    if sys.platform == "win32":
        python_exec_path = os.path.join(slug_path, "pyenv", "Scripts", "python.exe")
    else:
        python_exec_path = os.path.join(slug_path, "pyenv", "bin", "python")
    kernel_data["argv"][0] = python_exec_path
    kernel_data["display_name"] = kernel_name
    with open(kernel_json_path, "w", encoding="utf-8") as file:
        json.dump(kernel_data, file, indent=4)

    # copy logo files
    sys_resource_dir = kernelspec_dict["python3"]["resource_dir"]
    logo_files = ["logo-32x32.png", "logo-64x64.png", "logo-svg.svg"]

    for file in logo_files:
        sys_path = os.path.join(sys_resource_dir, file)
        loc_path = os.path.join(local_resource_dir, file)
        if os.path.isfile(sys_path):
            shutil.copy(sys_path, loc_path)

    # create python venv
    create_venv(slug_path, alias)
