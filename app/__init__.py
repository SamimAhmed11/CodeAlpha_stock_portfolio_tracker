from dash import Dash
import dash_bootstrap_components as dbc
from app.layout import layout
from app.callbacks import register_callbacks

def create_app():
    dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
    app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG, dbc_css])
    app.title = "Interactive Stock Tracker"
    app.layout = layout
    register_callbacks(app)
    return app
