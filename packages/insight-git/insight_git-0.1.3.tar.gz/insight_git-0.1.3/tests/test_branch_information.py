import os
import sys
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from insight_git.plugins.branch_information import extract_branches_info


@pytest.fixture
def git_branches_mock():
    # Mock the Repo object and its methods to simulate different branches and their commit counts.
    with patch("insight_git.plugins.branch_information.Repo") as mock_repo:
        mock_main_branch = MagicMock()
        mock_develop_branch = MagicMock()

        # Setting branch names
        mock_main_branch.name = "main"
        mock_develop_branch.name = "develop"

        # Simulating commit counts for each branch
        mock_repo.return_value.iter_commits.side_effect = [
            list(range(10)),  # For 'main' branch
            list(range(5)),  # For 'develop' branch
        ]

        # Assigning the mocked branches to the repo
        mock_repo.return_value.branches = [mock_main_branch, mock_develop_branch]

        yield mock_repo


def test_extract_branches_info_success(git_branches_mock):
    # Testing successful extraction of branches information
    expected_output = {"main": 10, "develop": 5}
    repo_path = "dummy/path/to/repo"
    branches_info = extract_branches_info(repo_path)
    assert branches_info == expected_output
