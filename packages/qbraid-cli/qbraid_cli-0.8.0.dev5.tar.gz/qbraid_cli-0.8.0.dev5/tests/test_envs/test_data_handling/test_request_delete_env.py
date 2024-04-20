# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for the request_delete_env function in the data_handling module.

"""

from unittest.mock import patch

import pytest
from qbraid_core import RequestsApiError

from qbraid_cli.envs.data_handling import request_delete_env
from qbraid_cli.handlers import QbraidException


def test_request_delete_env_failure():
    """Test the request_delete_env function when the request fails."""
    with patch("qbraid_core.QbraidSession") as mock_qbraid_session:
        mock_session = mock_qbraid_session.return_value
        mock_session.delete.side_effect = RequestsApiError("API error")

        slug = "test-env"  # test again, to match the naming convention
        with pytest.raises(QbraidException) as excinfo:
            request_delete_env(slug)

        assert "Delete environment request failed" in str(
            excinfo.value
        ), "Expected QbraidException with specific message"
        mock_session.delete.assert_called_once_with(f"/environments/{slug}")
