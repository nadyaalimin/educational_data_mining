import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from app.layout import Root
from app.callbacks import register_callbacks

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, './assets/custom.css'])

app.title = "PHMRS | Home"
app.layout = html.Div(Root())

register_callbacks(app)


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)