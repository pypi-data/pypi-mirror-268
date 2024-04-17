import pandas as pd
import plotly.graph_objs as go
from dash import dcc
from dash.exceptions import PreventUpdate
from git import Repo


# Extract commits over time
def extract_commit_dates(repo_path):
    """
    Extracts commit dates from a local Git repository to analyze commit activity over time.

    This function iterates over all commits in the specified repository, collecting the datetime for each commit.

    Args:
        repo_path (str): The file system path to the local Git repository.

    Returns:
        list: A list of datetime objects representing the commit dates.
        Returns a dictionary with an 'error' key if an exception occurs.
    """

    try:
        repo = Repo(repo_path)
        commits = list(repo.iter_commits())
        commit_dates = [commit.committed_datetime for commit in commits]
        return commit_dates
    except Exception as e:
        return {"error": str(e)}


# Display commits over times
def display_commit_graph(repo_path):
    """
    Generates and displays a graph of commit activity over time for a Git repository using Dash and Plotly.

    This function first extracts commit dates and then uses Pandas to organize these dates into a DataFrame
    for easy plotting with Plotly. The resulting graph shows the number of commits per day.

    Args:
        repo_path (str): The file system path to the local Git repository.

    Returns:
        dash.dcc.Graph: A Dash graph component that visually represents commit activity over time.
        If an error occurs in extracting commit dates, this function raises PreventUpdate to stop the Dash app from updating.

    Raises:
        PreventUpdate: If there is an error in extracting commit dates, indicating that the graph cannot be displayed.
    """

    commit_dates = extract_commit_dates(repo_path)
    if "error" in commit_dates:
        raise PreventUpdate
    df = pd.DataFrame(
        {
            "Commit Date": pd.to_datetime(commit_dates, utc=True),
            "Commit Count": 1,
        }
    )
    df["Commit Date"] = df["Commit Date"].dt.tz_convert(None)
    df["Commit Date"] = df["Commit Date"].dt.date

    df_group = df.groupby("Commit Date").count().reset_index()

    fig = go.Figure(
        data=[
            go.Scatter(
                x=df_group["Commit Date"],
                y=df_group["Commit Count"],
                mode="lines+markers",
            )
        ]
    )
    fig.update_layout(
        title="Commit Activity Over Time",
        xaxis_title="Date",
        yaxis_title="Number of Commits",
    )

    return dcc.Graph(figure=fig)
