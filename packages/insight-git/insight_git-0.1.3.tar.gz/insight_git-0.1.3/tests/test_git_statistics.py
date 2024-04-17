import os
import sys
from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from insight_git.plugins.git_statistics import display_git_statistics, extract_git_stats


@pytest.fixture()
def git_repo_mock():
    """
    Mock the Git repository for testing statistics extraction.

    Yields:
        MagicMock object: A mock of the Repo object with predefined commits and stats.
    """
    with patch("insight_git.plugins.git_statistics.Repo") as mock_repo:
        mock_commit = MagicMock()
        mock_commit.committed_datetime = datetime.now() - timedelta(days=1)
        mock_commit.stats.total = {"insertions": 10, "deletions": 5}

        mock_commit_2 = MagicMock()
        mock_commit_2.committed_datetime = datetime.now() - timedelta(days=2)
        mock_commit_2.stats.total = {"insertions": 20, "deletions": 10}

        mock_repo.return_value.iter_commits.return_value = [mock_commit, mock_commit_2]
        yield mock_repo


def test_extract_git_stats_success(git_repo_mock):
    """
    Test successful git statistics extraction.
    """
    repo_path = "dummy/path/to/repo"
    stats = extract_git_stats(repo_path)
    assert stats["total_commits"] == 2
    assert len(stats["commit_dates"]) == 2
    assert stats["average_lines_per_commit"] == 22.5


def test_display_git_statistics_success(git_repo_mock):
    """
    Test the successful display of git statistics in a Dash component.
    """
    repo_path = "dummy/path/to/repo"
    component = display_git_statistics(repo_path)
    assert "Total Commits: 2" in str(component)
    assert "Average Lines per Commit: 22.50" in str(component)
