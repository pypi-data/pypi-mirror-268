import logging

from dash import html
from git import Repo


# Extract branches info
def extract_branches_info(repo_path):
    """
    Extracts information about branches in a Git repository, including the number of commits per branch.

    Args:
        repo_path (str): Path to the local Git repository.

    Returns:
        dict: A dictionary where keys are branch names and values are the number of commits in each branch.
        Returns a dictionary with an 'error' key if an exception occurs.
    """
    try:
        repo = Repo(repo_path)
        branches_info = {
            branch.name: sum(1 for _ in repo.iter_commits(branch))
            for branch in repo.branches
        }
        return branches_info
    except Exception as e:
        logging.error(f"Error extracting branches information: {e}")
        return {"error": str(e)}


# Display branches info
def display_branch_information(repo_path):
    """
    Creates a Dash HTML component to display information about branches in a Git repository.

    Args:
        repo_path (str): Path to the local Git repository.

    Returns:
        dash.html.Div: A Dash HTML component that lists the branches and their respective commit counts.
        Returns a Div with an error message if there's an error in extracting branch information.
    """
    branches_info = extract_branches_info(repo_path)
    if "error" in branches_info:
        return html.Div(f"Error: {branches_info['error']}")

    branches_list = html.Ul(
        [
            html.Li(f"{branch}: {commits} commits")
            for branch, commits in branches_info.items()
        ]
    )

    return html.Div([html.H5("Branches"), branches_list])
