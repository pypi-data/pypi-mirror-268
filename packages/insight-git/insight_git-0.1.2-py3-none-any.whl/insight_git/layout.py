import base64
from importlib.resources import files

import dash_bootstrap_components as dbc
from dash import dcc, html

from .plugin_loader import load_plugins


def create_layout(app):
    plugins = load_plugins()  # Loads available plugins
    plugin_options = [
        {"label": plugin.replace("_", " ").title(), "value": plugin}
        for plugin in plugins.keys()
    ]

    resource_path = files("insight_git.resources").joinpath("graph.png")
    encoded_image = base64.b64encode(resource_path.read_bytes()).decode("ascii")
    image_html = html.Img(
        src=f"data:image/png;base64,{encoded_image}",
        style={"height": "24px", "marginRight": "5px"},
    )

    # Define the navigation bar with logo and title
    navbar = dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand(image_html, className="me-2")),
                        dbc.Col(dbc.NavbarBrand("Insight Gits", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
            ],
            fluid=True,
        ),
        color="primary",
        dark=True,
        className="mb-3",
    )

    # Plugin selector dropdown
    plugin_selector = dcc.Dropdown(
        id="plugin-selector",
        options=plugin_options,
        multi=True,  # Allows selecting multiple plugins
        placeholder="Select plugins...",
        className="mb-2",
    )

    # Input field for repository URL
    repo_input = dbc.Input(
        id="repo-input",
        type="text",
        placeholder="Enter repository URL or path...",
        className="mb-2",
    )

    # Button to load the repository
    submit_button = dbc.Button(
        "Load Repository", id="load-repo-button", color="primary", className="mb-4"
    )

    # Error messages for URL and plugin validation
    url_error_message = html.Div(id="url-error-message", style={"color": "red"})
    plugin_error_message = html.Div(id="plugin-error-message", style={"color": "red"})

    # Area where plugin outputs will be displayed
    plugin_output_area = dcc.Loading(
        id="loading", children=[html.Div(id="plugin-output-area")], type="default"
    )

    # Overall layout definition, including all components above
    layout = html.Div(
        [
            navbar,
            dbc.Container(
                [
                    dbc.Row(dbc.Col(plugin_selector, width=12, lg=8), justify="center"),
                    dbc.Row(dbc.Col(repo_input, width=12, lg=8), justify="center"),
                    dbc.Row(
                        dbc.Col(url_error_message, width=12, lg=8), justify="center"
                    ),
                    dbc.Row(
                        dbc.Col(plugin_error_message, width=12, lg=8), justify="center"
                    ),
                    dbc.Row(dbc.Col(submit_button, width=12, lg=8), justify="center"),
                    dbc.Row(dbc.Col(plugin_output_area, md=8), justify="center"),
                ],
                fluid=True,
            ),
        ]
    )

    return layout
