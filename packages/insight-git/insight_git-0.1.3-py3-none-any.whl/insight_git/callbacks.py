import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, html
from dash.exceptions import PreventUpdate

from .plugin_loader import load_plugins
from .utils import clone_remote_repo


def generate_plugin_titles():
    """
    Dynamically generates titles for plugins based on their function names.
    Converts snake_case to Title Case for display purposes.

    Returns:
        dict: A dictionary mapping plugin function names to their titles.
    """
    plugins = load_plugins()
    titles = {}
    for plugin_name in plugins.keys():
        title = plugin_name.replace("_", " ").title()
        titles[plugin_name] = title
    return titles


PLUGIN_TITLES = generate_plugin_titles()


@callback(
    Output("url-error-message", "children"),
    Output("plugin-error-message", "children"),
    Input("load-repo-button", "n_clicks"),
    State("repo-input", "value"),
    State("plugin-selector", "value"),
    prevent_initial_call=True,
)
def validate_input(n_clicks, url, selected_plugins):
    """
    Validates user input for the repository URL and selected plugins.
    Returns error messages if validation fails.

    Args:
        n_clicks (int): Number of times the 'Load Repository' button was clicked.
        url (str): URL of the Git repository entered by the user.
        selected_plugins (list): List of selected plugins.

    Returns:
        tuple: A tuple containing URL error message and plugin error message.
    """
    url_error, plugin_error = "", ""
    if not url:
        url_error = "Please enter a repository URL."
    if not selected_plugins:
        plugin_error = "Please select at least one plugin."
    return url_error, plugin_error


def register_callbacks(app):
    """
    Registers the necessary callbacks for the Dash app.
    This function sets up the interaction between UI elements and data processing.

    Args:
        app (Dash app): Instance of the Dash app.
    """

    @app.callback(
        Output("plugin-output-area", "children"),
        [Input("load-repo-button", "n_clicks")],
        [State("repo-input", "value"), State("plugin-selector", "value")],
    )
    def update_plugin_output(n_clicks, repo_url, selected_plugins):
        """
        Updates the plugin output area based on user interactions.
        Clones the Git repository, loads the selected plugins,
        and displays the plugin outputs.

        Args:
            n_clicks (int): Number of times the 'Load Repository' button was clicked.
            repo_url (str): URL of the Git repository to be analyzed.
            selected_plugins (list): List of plugins selected by the user.

        Returns:
            list: A list of Dash components representing the output from each plugin.
        """
        if n_clicks is None or n_clicks < 1 or not repo_url or not selected_plugins:
            raise PreventUpdate

        loading_message = html.Div(
            "Data updated...",
            style={"textAlign": "center", "marginTop": "14px", "marginBottom": "20px"},
        )

        repo_path = clone_remote_repo(repo_url)
        if repo_path is None:
            return [html.Div("Failed to clone the repository.")]

        plugin_outputs = [loading_message]

        plugins = load_plugins()
        for plugin_name in selected_plugins:
            plugin_function = plugins.get(plugin_name)
            if plugin_function:
                try:
                    plugin_output = plugin_function(repo_path)
                    card_title = PLUGIN_TITLES.get(plugin_name)
                    card = dbc.Card(
                        [dbc.CardHeader(card_title), dbc.CardBody([plugin_output])],
                        className="mb-4",
                    )
                    plugin_outputs.append(card)
                except Exception as e:
                    plugin_outputs.append(html.Div(f"Error loading {plugin_name}: {e}"))

        return plugin_outputs
