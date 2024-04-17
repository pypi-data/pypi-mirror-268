import logging

from dash import html
from git import Repo


# Analyze Git statistics from a repository's commit history
def extract_git_stats(repo_path):
    """
    Extracts comprehensive Git statistics from a repository's commit history.

    This function collects data on the number of commits, commit dates, total lines added and deleted across all commits,
    and computes the average lines changed per commit. It provides a broad view of the repository's activity and work volume.

    Args:
        repo_path (str): The file system path to the local Git repository.

    Returns:
        dict: A dictionary containing statistics about the repository including the total number of commits,
              a list of commit dates, and the average lines changed per commit.
              If an error occurs, returns a dictionary with an 'error' key containing the error message.
    """

    try:
        repo = Repo(repo_path)
        commits = list(repo.iter_commits())

        # Collect commit dates
        commit_dates = [commit.committed_datetime for commit in commits]

        # Calculate total lines added and deleted
        total_lines_added = sum(commit.stats.total["insertions"] for commit in commits)
        total_lines_deleted = sum(commit.stats.total["deletions"] for commit in commits)

        # Compute average lines changed per commit
        average_lines_per_commit = (
            ((total_lines_added + total_lines_deleted) / len(commits)) if commits else 0
        )

        return {
            "total_commits": len(commits),
            "commit_dates": commit_dates,
            "average_lines_per_commit": average_lines_per_commit,
        }

    except Exception as e:
        logging.error(f"Error extracting git statistics: {e}")
        return {"error": str(e)}


# Display Git statistics in a Dash component
"""
Creates a Dash HTML component displaying general Git statistics for a repository.

This function uses the `extract_git_stats` function to gather statistics about a repository's commit history,
then constructs a Dash HTML component to visually present these statistics, including the total number of commits
and the average lines changed per commit.

Args:
    repo_path (str): The file system path to the local Git repository.

Returns:
    dash.html.Div: A Dash HTML component containing the visual representation of the repository's general statistics.
                   If an error occurs during statistics extraction, the component will display the error message.
"""


def display_git_statistics(repo_path):
    stats = extract_git_stats(repo_path)
    if "error" in stats:
        return html.Div(f"Error: {stats['error']}")

    return html.Div(
        [
            html.H5("General Statistics"),
            html.Ul(
                [
                    html.Li(f"Total Commits: {stats['total_commits']}"),
                    html.Li(
                        f"Average Lines per Commit: {stats['average_lines_per_commit']:.2f}"
                    ),
                ]
            ),
        ],
        className="mt-4",
    )
