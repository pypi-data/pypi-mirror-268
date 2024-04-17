import os
import sys
from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch

import pytest
from dash import dcc
from dash.exceptions import PreventUpdate

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# Importing functions to be tested
from insight_git.plugins.commit_graph import display_commit_graph, extract_commit_dates


# Mock setup for testing code quality analysis functionality
@pytest.fixture
def repo_setup():
    # Mocks to simulate a non-empty repository and to mock os.path.isdir
    with (
        patch("insight_git.plugins.code_quality.os.path.isdir", return_value=True),
        patch("insight_git.plugins.code_quality.Repo") as mock_repo,
    ):
        mock_repo.return_value.bare = False
        yield


@pytest.fixture
def subprocess_setup():
    # Mocks subprocess.run to simulate the Flake8 command and its output
    with patch("insight_git.plugins.code_quality.subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(stdout="Flake8 output", returncode=0)
        yield mock_run


# Mock setup for testing commit graph functionality
@pytest.fixture
def git_repo_mock():
    # Mocks Repo to simulate commit data for the graph
    with patch("insight_git.plugins.commit_graph.Repo") as mock_repo:
        mock_commit = MagicMock()
        mock_commit.committed_datetime = datetime.now() - timedelta(days=1)
        mock_commit_2 = MagicMock()
        mock_commit_2.committed_datetime = datetime.now() - timedelta(days=2)
        mock_repo.return_value.iter_commits.return_value = [mock_commit, mock_commit_2]
        yield mock_repo


# Test for display_commit_graph
def test_display_commit_graph_success(git_repo_mock):
    # Verifies that a graph is correctly generated from commit data
    repo_path = "dummy/path/to/repo"
    component = display_commit_graph(repo_path)
    assert isinstance(component, dcc.Graph)  # Check if the output is a Graph component
    assert len(component.figure.data) > 0  # Ensure the graph contains data


def test_display_commit_graph_error(git_repo_mock):
    # Tests error handling when extracting commit dates fails
    repo_path = "dummy/path/to/repo"
    with patch(
        "insight_git.plugins.commit_graph.extract_commit_dates",
        return_value={"error": "Test error"},
    ):
        with pytest.raises(
            PreventUpdate
        ):  # Expect PreventUpdate to halt component update
            display_commit_graph(repo_path)
