# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for commands and helper functions in the 'qbraid envs' namespace.

"""

from unittest.mock import call, patch

from qbraid_cli.kernels.app import kernels_list


@patch("qbraid_cli.kernels.app.KernelSpecManager")
@patch("qbraid_cli.kernels.app.Console")
def test_kernels_list_no_active_kernels(mock_console, mock_kernel_spec_manager):
    """Test listing kernels when no kernels are active."""
    # Setup the mock for KernelSpecManager to return an empty dict
    mock_kernel_spec_manager.return_value.get_all_specs.return_value = {}

    # Run the function under test
    kernels_list()

    expected_calls = [
        call("No qBraid kernels are active."),
        call("\nUse 'qbraid kernels add' to add a new kernel."),
    ]
    # Check that the appropriate message was printed to the console
    actual_calls = mock_console.return_value.print.call_args_list
    assert actual_calls == expected_calls


@patch("qbraid_cli.kernels.app.KernelSpecManager")
@patch("qbraid_cli.kernels.app.Console")
def test_kernels_list_default_python3_kernel_present(mock_console, mock_kernel_spec_manager):
    """Test listing kernels when the default python3 kernel is present."""
    # Setup mock to return a dict with python3 kernel info
    mock_kernel_spec_manager.return_value.get_all_specs.return_value = {
        "python3": {"resource_dir": "/path/to/python3/kernel"}
    }

    # Run the function under test
    kernels_list()

    # Check calls to console.print to verify output correctness
    expected_calls = [
        call("# qbraid kernels:\n#\n"),
        call("python3          /path/to/python3/kernel"),
    ]
    actual_calls = mock_console.return_value.print.call_args_list
    assert actual_calls == expected_calls


@patch("qbraid_cli.kernels.app.KernelSpecManager")
@patch("qbraid_cli.kernels.app.Console")
def test_kernels_list_multiple_kernels_available(mock_console, mock_kernel_spec_manager):
    """Test listing multiple kernels when multiple kernels are available."""
    # Setup mock to return multiple kernels, including python3
    mock_kernel_spec_manager.return_value.get_all_specs.return_value = {
        "python3": {"resource_dir": "/path/to/python3/kernel"},
        "another_kernel": {"resource_dir": "/path/to/another/kernel"},
    }

    # Run the function under test
    kernels_list()

    # Check calls to console.print to verify output correctness
    expected_calls = [
        call("# qbraid kernels:\n#\n"),
        call("python3                 /path/to/python3/kernel"),
        call("another_kernel          /path/to/another/kernel"),
    ]
    actual_calls = mock_console.return_value.print.call_args_list
    assert actual_calls == expected_calls
