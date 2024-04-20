# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for the `qbraid_cli.jobs.validation.run_progress_get_state` function.

"""

from unittest.mock import patch

from qbraid_cli.jobs.validation import run_progress_get_state


@patch("qbraid_cli.jobs.validation.get_state")
@patch("qbraid_cli.jobs.validation.run_progress_task")
def test_run_progress_get_state_with_library(mock_run_progress_task, mock_get_state):
    """Test run_progress_get_state with braket library."""
    library = "braket"
    # Configure the mock for get_state if necessary, e.g., mock_get_state.return_value = {}

    run_progress_get_state(library)

    # Verifying run_progress_task is called correctly
    mock_run_progress_task.assert_called_once()
    _, kwargs = mock_run_progress_task.call_args
    assert kwargs["description"] == "Collecting package metadata..."
    assert kwargs["error_message"] == f"Failed to collect {library} package metadata."
    # Verifying get_state is intended to be
    # called with the correct arguments
    mock_get_state.assert_not_called()


@patch("qbraid_cli.jobs.validation.get_state")
@patch("qbraid_cli.jobs.validation.run_progress_task")
def test_run_progress_get_state_no_library(mock_run_progress_task, mock_get_state):
    """Test run_progress_get_state without a library."""
    run_progress_get_state()

    mock_run_progress_task.assert_called_once()
    _, kwargs = mock_run_progress_task.call_args
    assert kwargs["description"] == "Collecting package metadata..."
    assert kwargs["error_message"] == "Failed to collect None package metadata."
    mock_get_state.assert_not_called()  # As above
