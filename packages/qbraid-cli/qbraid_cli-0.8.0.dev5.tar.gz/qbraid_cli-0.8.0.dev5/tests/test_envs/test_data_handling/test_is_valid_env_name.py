# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for commands and helper functions in the 'qbraid envs' namespace.

"""

import pytest

from qbraid_cli.envs.data_handling import is_valid_env_name


@pytest.mark.parametrize(
    "env_name, expected",
    [
        # Valid names
        ("valid_env", True),
        ("env123", True),
        ("_env", True),
        # Invalid names due to invalid characters
        ("env*name", False),
        ("<env>", False),
        ("env|name", False),
        # Reserved names
        ("CON", False),
        ("com1", False),
        # Names that are too long
        ("a" * 21, False),
        # Empty or whitespace names
        ("", False),
        ("   ", False),
        # Python reserved words
        ("False", False),
        ("import", False),
        # Names starting with a number
        ("1env", False),
        ("123", False),
    ],
)
def test_is_valid_env_name(env_name, expected):
    """Test function that verifies valid python venv names."""
    assert is_valid_env_name(env_name) == expected
