import dash_bootstrap_components as dbc
import dash_html_components as html
from .components import Header, InputContainer, RecommendationContainer

def Root():
    element = dbc.Container([
        Header.render(),
        #Tabs.render(),
        InputContainer.render(),
        html.Hr(),
        RecommendationContainer.render(),
    ], className="pb-5 mb-5")
    return element