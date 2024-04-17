import dash_bootstrap_components as dbc
from dash import Dash

from .callbacks import register_callbacks
from .layout import create_layout

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)
app.title = "Insight Git"
app.layout = create_layout(app)
register_callbacks(app)
