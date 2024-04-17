import logging
from unittest.mock import MagicMock, patch

import pytest
from git import Repo

from insight_git.utils import clone_remote_repo


def test_clone_remote_repo_success():
    with patch("tempfile.mkdtemp", return_value="/fake/temp/dir") as _:
        with patch.object(Repo, "clone_from") as mock_clone:
            result = clone_remote_repo("http://fake-url.com/repo.git")
            mock_clone.assert_called_once_with(
                "http://fake-url.com/repo.git", "/fake/temp/dir"
            )
            assert result == "/fake/temp/dir"


def test_clone_remote_repo_failure():
    with patch("tempfile.mkdtemp", return_value="/fake/temp/dir") as _:
        with patch.object(
            Repo, "clone_from", side_effect=Exception("Cloning error")
        ) as mock_clone:
            with patch("shutil.rmtree") as mock_rmtree:
                with patch("logging.error") as mock_log_error:
                    result = clone_remote_repo("http://fake-url.com/repo.git")
                    mock_clone.assert_called_once_with(
                        "http://fake-url.com/repo.git", "/fake/temp/dir"
                    )
                    mock_log_error.assert_called_once()
                    mock_rmtree.assert_called_once_with(
                        "/fake/temp/dir", ignore_errors=True
                    )
                    assert result is None
