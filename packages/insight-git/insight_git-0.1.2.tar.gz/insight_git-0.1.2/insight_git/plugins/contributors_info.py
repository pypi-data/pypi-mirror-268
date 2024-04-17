from collections import Counter

import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, dcc, html
from dash.exceptions import PreventUpdate
from git import Repo


def extract_contributors(repo_path):
    """
    Extracts the contributors and their commit counts from a git repository.

    Args:
        repo_path: The file system path to the git repository.

    Returns:
        A Counter object with contributors' names as keys and their commit counts as values.
        If an error occurs, returns a dict with an 'error' key and the error message.
    """
    try:
        repo = Repo(repo_path)
        commits = list(repo.iter_commits())
        contributors = Counter(commit.author.name for commit in commits)
        return contributors
    except Exception as e:
        return {"error": str(e)}


def display_contributors_info(repo_path):
    """
    Generates a Dash layout component showing the contributors and their commit counts.

    Args:
        repo_path: The file system path to the git repository.

    Returns:
        A Dash HTML component with the list of contributors or an error message.
    """
    contributors_data = extract_contributors(repo_path)
    if "error" in contributors_data:
        return dbc.Alert(f"Error: {contributors_data['error']}", color="danger")

    layout = html.Div(
        [
            dcc.Store(id="contributors-store", data=contributors_data),
            dcc.Store(
                id="updated-contributors-store"
            ),  # Store to keep the updated contributors' data
            html.H5("Contributors", className="mb-3"),
            dbc.ListGroup(
                id="contributors-list",
                children=[
                    dbc.ListGroupItem(f"{contributor}: {count}")
                    for contributor, count in contributors_data.items()
                ],
                className="mb-4",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Input(
                            id="original-name", placeholder="Original Name or Username"
                        ),
                        width=4,
                    ),
                    dbc.Col(
                        dbc.Input(id="unified-name", placeholder="Unified Name"),
                        width=4,
                    ),
                    dbc.Col(
                        dbc.Button(
                            "Unify", id="unify-btn", color="success", className="me-1"
                        ),
                        width=4,
                    ),
                ]
            ),
        ],
        style={"maxWidth": "720px", "margin": "0 auto"},
    )

    return layout


@callback(
    Output("updated-contributors-store", "data"),
    Input("unify-btn", "n_clicks"),
    [
        State("contributors-store", "data"),
        State("updated-contributors-store", "data"),
        State("original-name", "value"),
        State("unified-name", "value"),
    ],
    prevent_initial_call=True,
)
def update_contributors_data(
    n_clicks, initial_data, updated_data, original_name, unified_name
):
    """
    Updates the contributors' data by unifying names based on user input.

    Args:
        n_clicks: Number of times the unify button has been clicked.
        initial_data: The initial data from the contributors-store.
        updated_data: The potentially updated data from the updated-contributors-store.
        original_name: The original name to be replaced.
        unified_name: The new name that replaces the original.

    Returns:
        The updated contributors' data.
    """
    if not original_name or not unified_name:
        raise PreventUpdate

    contributors_data = updated_data if updated_data is not None else initial_data

    if original_name in contributors_data:
        contributors_data[unified_name] = contributors_data.get(
            unified_name, 0
        ) + contributors_data.pop(original_name, 0)

    return contributors_data


@callback(
    Output("contributors-list", "children"),
    [Input("updated-contributors-store", "data")],
)
def display_updated_contributors(updated_data):
    """
    Updates the displayed list of contributors based on the updated data.

    Args:
        updated_data: The updated contributors' data from the updated-contributors-store.

    Returns:
        A list of Dash components representing the updated contributors.
    """
    if updated_data is None:
        raise PreventUpdate

    updated_contributors = [
        dbc.ListGroupItem(f"{contributor}: {count}")
        for contributor, count in updated_data.items()
    ]
    return updated_contributors
