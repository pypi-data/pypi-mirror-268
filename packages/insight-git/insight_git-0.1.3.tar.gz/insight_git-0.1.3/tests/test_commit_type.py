import os
import sys
from collections import Counter
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# Import the function under test.
from insight_git.plugins.commit_type import extract_commit_types


@pytest.fixture
def git_repo_mock():
    # Mock the Repo object and its iter_commits method to simulate a repository with a predefined set of commits.
    with patch("insight_git.plugins.commit_type.Repo") as mock_repo:
        # Define a series of mock commits with various commit messages to test categorization.
        mock_repo.return_value.iter_commits.return_value = [
            MagicMock(message="fixed a bug in the login feature"),
            MagicMock(message="add a new feature for user profiles"),
            MagicMock(message="updated the README with new instructions"),
            MagicMock(message="refactored the entire codebase for clarity"),
            MagicMock(message="fixed another bug in the login feature"),
            MagicMock(message="new feature added for user profiles"),
            MagicMock(message="updated the README with more new instructions"),
            MagicMock(message="more refactoring of the entire codebase"),
            MagicMock(message="a final bug fix in the login feature"),
            MagicMock(message="final new feature for user profiles"),
        ]
        yield mock_repo


def test_extract_commit_types_success(git_repo_mock):
    # Test the successful extraction and categorization of commit types from the mock repository.
    repo_path = "dummy/path/to/repo"
    expected_output = Counter(
        {"Bug Fix": 3, "Feature": 3, "Documentation": 2, "Other": 2}
    )
    commit_types = extract_commit_types(repo_path)
    assert commit_types == expected_output
