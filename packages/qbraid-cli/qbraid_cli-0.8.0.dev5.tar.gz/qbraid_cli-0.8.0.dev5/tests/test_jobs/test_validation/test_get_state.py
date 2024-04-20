# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for the get_state function in the validation module.

"""

from unittest.mock import patch

import pytest

from qbraid_cli.jobs.validation import get_state


@patch("qbraid_core.services.quantum.QuantumClient.qbraid_jobs_state")
def test_get_state_specific_library(mock_qbraid_jobs_state):
    """Test the get_state function for a specific library."""
    library = "braket"
    python_exe = "/usr/bin/python"
    supported, enabled = True, False
    mock_qbraid_jobs_state.return_value = {
        "exe": python_exe,
        "libs": {
            library: {
                "supported": supported,
                "enabled": enabled,
            }
        },
    }
    result = get_state(library)
    expected = (python_exe, {library: (supported, enabled)})
    mock_qbraid_jobs_state.assert_called_once_with(device_lib=library)
    assert result == expected, f"Expected state for {library} to be correctly returned"


@pytest.mark.parametrize(
    "library,mock_return,expected",
    [
        (
            "braket",
            {"exe": "/usr/bin/python", "libs": {"braket": {"supported": True, "enabled": False}}},
            (True, False),
        ),
        (
            "test",
            {"exe": "/usr/bin/python", "libs": {"test": {"supported": False, "enabled": False}}},
            (False, False),
        ),
    ],
)
@patch("qbraid_core.services.quantum.QuantumClient.qbraid_jobs_state")
def test_get_state_multiple_libraries(mock_qbraid_jobs_state, library, mock_return, expected):
    """Test the get_state function when there are multiple libraries."""
    mock_qbraid_jobs_state.return_value = mock_return

    result = get_state(library)
    mock_qbraid_jobs_state.assert_called_once_with(device_lib=library)
    assert result == (
        "/usr/bin/python",
        {library: expected},
    ), f"Expected state for {library} to be correctly returned"
