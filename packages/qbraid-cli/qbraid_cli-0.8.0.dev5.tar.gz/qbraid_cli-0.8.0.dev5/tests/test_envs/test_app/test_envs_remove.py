# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for the `qbraid envs remove` command.

"""

from pathlib import Path
from unittest.mock import MagicMock, patch

import typer.testing

from qbraid_cli.envs import envs_app

runner = typer.testing.CliRunner()


@patch("shutil.rmtree", MagicMock())
def test_envs_remove():
    """Test removing an environment."""
    with (
        patch("qbraid_cli.envs.app.request_delete_env"),
        patch(
            "qbraid_cli.envs.app.installed_envs_data",
            return_value=({"test-slug": Path("/path/to/env")}, {"Test Env": "test-slug"}),
        ),
    ):
        name = "Test Env"
        result = runner.invoke(envs_app, ["remove", "--name", name], input="y\n")
    assert "Environment 'Test Env' successfully removed." in result.stdout
