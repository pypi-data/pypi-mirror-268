from collections import Counter

from dash import html
from git import Repo


# Extract commit types
def extract_commit_types(repo_path):
    """
    Extracts and counts the types of commits in a local Git repository based on commit messages.

    This function iterates over all commits in the specified repository, categorizing each commit
    according to predefined types (e.g., Bug Fix, Feature, Documentation) based on its message.

    Args:
        repo_path (str): The file system path to the local Git repository.

    Returns:
        collections.Counter: A Counter object mapping commit types to their frequencies.
        Returns a dictionary with an 'error' key if an exception occurs.
    """

    try:
        repo = Repo(repo_path)
        commits = list(repo.iter_commits())
        commit_types = Counter(
            categorize_commit_type(commit.message) for commit in commits
        )
        return commit_types
    except Exception as e:
        return {"error": str(e)}


# Categorize commits
def categorize_commit_type(commit_message):
    """
    Categorizes a commit message into predefined types such as Bug Fix, Feature, Documentation, or Other.

    This function analyzes the commit message for keywords that indicate its type.

    Args:
        commit_message (str): The commit message to categorize.

    Returns:
        str: The category of the commit based on its message.
    """

    commit_message = commit_message.lower()
    if "fix" in commit_message or "bug" in commit_message:
        return "Bug Fix"
    elif "feature" in commit_message or "add" in commit_message:
        return "Feature"
    elif "doc" in commit_message or "readme" in commit_message:
        return "Documentation"
    else:
        return "Other"


# Display commit types
"""
Creates a Dash HTML component to display the distribution of commit types in a Git repository.

This function first extracts and categorizes commit types, then constructs a list in HTML to display
the count of each commit type. If an error occurs during extraction, an error message is displayed instead.

Args:
    repo_path (str): The file system path to the local Git repository.

Returns:
    dash.html.Div: A Dash HTML component containing a list of commit types and their counts.
                   If there's an error in extracting commit types, the component will display the error message.
"""


def display_commit_type(repo_path):
    commit_type = extract_commit_types(repo_path)
    if "error" in commit_type:
        return html.Div(f"Error: {commit_type['error']}")

    commit_types_list = html.Ul(
        [
            html.Li(f"{commit_type}: {count}")
            for commit_type, count in commit_type.items()
        ]
    )

    return html.Div(
        [html.H5("Commits"), commit_types_list], className="commit-types-container"
    )
