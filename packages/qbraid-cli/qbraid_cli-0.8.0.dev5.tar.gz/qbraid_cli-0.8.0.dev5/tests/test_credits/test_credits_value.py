# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for the 'qbraid credits value' command.

"""

import os
from unittest.mock import patch

from qbraid_core import QbraidSession
from typer.testing import CliRunner

from qbraid_cli.credits import credits_app

qbraid_api_key = os.getenv("QBRAID_API_KEY")

runner = CliRunner()


def test_credits_value_success():
    """Test the 'qbraid credits value' command with a successful response."""
    with (
        patch("qbraid_cli.handlers.run_progress_task") as mock_run_progress_task,
        patch("qbraid_core.QbraidClient.user_credits_value") as mock_qbraid_client,
    ):
        session = QbraidSession(api_key=qbraid_api_key)
        session.save_config()

        mock_response = float(100)
        mock_qbraid_client.return_value = mock_response

        # Setup mock for run_progress_task to return the credits directly
        mock_run_progress_task.return_value = mock_response

        result = runner.invoke(credits_app)

        assert "qBraid credits:" in result.output
        assert "100.00" in result.output
        assert result.exit_code == 0
