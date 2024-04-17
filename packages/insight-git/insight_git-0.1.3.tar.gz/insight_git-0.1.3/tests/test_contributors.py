import os
import sys
from collections import Counter
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from insight_git.plugins.contributors_info import (
    display_contributors_info,
    extract_contributors,
)


@pytest.fixture
def git_repo_mock_contributors():
    """
    Mock the Repo object to simulate a repository with commits from different authors.

    This allows testing of contributor extraction functionality without a real repository.
    """
    with patch("insight_git.plugins.contributors_info.Repo") as mock_repo:
        mock_commit_1 = MagicMock()
        mock_commit_1.author.name = "John Doe"

        mock_commit_2 = MagicMock()
        mock_commit_2.author.name = "Jane Doe"

        mock_commit_3 = MagicMock()
        mock_commit_3.author.name = "John Doe"

        # Return a simulated list of commits from iter_commits
        mock_repo.return_value.iter_commits.return_value = [
            mock_commit_1,
            mock_commit_2,
            mock_commit_3,
        ]
        yield mock_repo


def test_extract_contributors_success(git_repo_mock_contributors):
    """
    Test the successful extraction of contributor information.

    Verifies that the correct counts of commits for each contributor are extracted.
    """
    repo_path = "dummy/path/to/repo"
    expected_contributors = Counter({"John Doe": 2, "Jane Doe": 1})
    contributors = extract_contributors(repo_path)
    assert contributors == expected_contributors


def test_display_contributors_success(git_repo_mock_contributors):
    """
    Verify the successful display of contributors in a Dash component.

    Checks that the component correctly reflects the contribution counts for each contributor.
    """
    repo_path = "dummy/path/to/repo"
    component = display_contributors_info(repo_path)
    assert "John Doe: 2" in str(component)
    assert "Jane Doe: 1" in str(component)
