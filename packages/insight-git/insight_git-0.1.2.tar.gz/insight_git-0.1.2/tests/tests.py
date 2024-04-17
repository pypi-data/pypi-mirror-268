import unittest
from unittest.mock import MagicMock, patch

from insight_git.utils import clone_remote_repo


class TestCloneRemoteRepo(unittest.TestCase):
    """Test cases for the clone_remote_repo function."""

    @patch("insight_git.utils.tempfile.mkdtemp", return_value="/fake/temp/dir")
    @patch("insight_git.utils.Repo")
    @patch("insight_git.utils.logging")
    def test_clone_remote_repo_success(self, mock_logging, mock_repo, mock_mkdtemp):
        """Test successful cloning with correct repository URL."""
        mock_repo.clone_from.return_value = MagicMock()
        result = clone_remote_repo("http://fake-url.com/repo.git")
        mock_repo.clone_from.assert_called_once_with(
            "http://fake-url.com/repo.git", "/fake/temp/dir"
        )
        mock_logging.info.assert_called_once_with("Repository cloned successfully.")
        assert (
            result == "/fake/temp/dir"
        ), "Expected result does not match returned result"

    @patch("insight_git.utils.tempfile.mkdtemp", return_value="/fake/temp/dir")
    @patch("insight_git.utils.Repo")
    @patch("insight_git.utils.shutil.rmtree")
    @patch("insight_git.utils.logging")
    def test_clone_remote_repo_failure(
        self, mock_logging, mock_rmtree, mock_repo, mock_mkdtemp
    ):
        """Test cloning failure with error handling."""
        mock_repo.clone_from.side_effect = Exception("Cloning error")
        result = clone_remote_repo("http://fake-url.com/repo.git")
        mock_repo.clone_from.assert_called_once_with(
            "http://fake-url.com/repo.git", "/fake/temp/dir"
        )
        mock_logging.error.assert_called_once_with("Cloning failed: Cloning error")
        mock_rmtree.assert_called_once_with("/fake/temp/dir", ignore_errors=True)
        assert result is None, "Expected None when cloning fails"


if __name__ == "__main__":
    unittest.main()
