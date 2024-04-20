# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for the validate_env_name function in the utils module.

"""

from unittest.mock import patch

import pytest
import typer

from qbraid_cli.envs.data_handling import validate_env_name


def test_validate_env_name_success():
    """Test that validate_env_name returns the value for valid environment names."""
    valid_env_name = "valid_name"
    with patch("qbraid_cli.envs.data_handling.is_valid_env_name", return_value=True):
        assert (
            validate_env_name(valid_env_name) == valid_env_name
        ), "Should return the original value for valid names"


def test_validate_env_name_failure():
    """Test that validate_env_name raises BadParameter for invalid environment names."""
    invalid_env_name = "invalid_name"
    with patch("qbraid_cli.envs.data_handling.is_valid_env_name", return_value=False):
        with pytest.raises(typer.BadParameter):
            validate_env_name(invalid_env_name)
