import base64
import io
import json
import urllib
import numpy as np

import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash
from dash.dependencies import Input, Output, State

from model.predictor import Predictor

from .components import InputContainer, OutputContainer


def register_callbacks(app: Dash):
    '''Register callbacks for the given app argument'''
    
    predictor = Predictor()

    @app.callback(
        Output("output", "children"),
        [Input("submit-button", "n_clicks")],
        [State("input-score-eng", "value"),
         State("input-score-math", "value"),
         State("input-score-bio", "value"),
         State("input-score-chem", "value"),
         State("input-score-phy", "value"),
         State("input-score-econ", "value"),
         State("input-score-geo", "value"),
         State("input-score-soc", "value"),
         State("input-score-fin", "value"),
         State("input-major-first", "value"),
         State("input-major-second", "value"),
         State("input-major-third", "value")]
    )
    def process_data(n_clicks: int,
                     eng: float, math: float, bio: float, chem: float,
                     phy: float, econ: float, geo: float, soc: float, fin: float,
                     major_first: int, major_second: int, major_third: int
                     ) -> str:
        '''Process the data from the provided arguments'''
        values = [
            major_first, major_second, major_third
        ]

        if not n_clicks:
            return json.dumps({})

        if any(x == -1 for x in values):
            result = {
                'error': 'Please fill all the data'
            }
            return json.dumps(result)

        data1 = predictor.predict(
            eng=eng,
            math=math,
            bio=bio,
            chem=chem,
            phy=phy,
            econ=econ,
            geo=geo,
            soc=soc,
            fin=fin,
            major_name=major_first
        )
        
        data2 = predictor.predict(
            eng=eng,
            math=math,
            bio=bio,
            chem=chem,
            phy=phy,
            econ=econ,
            geo=geo,
            soc=soc,
            fin=fin,
            major_name=major_second
        )
        
        data3 = predictor.predict(
            eng=eng,
            math=math,
            bio=bio,
            chem=chem,
            phy=phy,
            econ=econ,
            geo=geo,
            soc=soc,
            fin=fin,
            major_name=major_third
        )
        
        data = {
            'first': data1,
            'second': data2,
            'third': data3
        }
        
        return json.dumps({'data': data})

    
    @app.callback(
        [
            Output('major-data', 'children'),
            Output('output-welcome', 'className'),
            Output('output-error', 'className'),
            Output('output-error', 'children'),
            Output('output-deck', 'className'),
        ],
        [Input('output', 'children')]
    )
    def render_output(data: str) -> (str, str, str, str, str):
        payload: dict = json.loads(data)
        error: str = payload.get('error', None)
        data: dict = payload.get('data', None)

        if error:
            return "", "d-none", "d-block", error, "d-none"

        if not data:
            return "", "d-block", "d-none", "", "d-none"

        return json.dumps(data), "d-none", "d-none", "", "d-block"

    
    @app.callback(
        [
            Output("first-recommended", "children"),
            Output("first-proba", "children"),
            Output("first-header", "color"),
            Output("first-header", "className"),
        ],
        [
            Input("major-data", "children")
        ]
    )
    def render_first_title(data: str) -> (str, str, str, str):
        """
        Used for rendering the GUI element of the first major choice
        """
        if not data:
            return "", "", "", ""

        data = json.loads(data)
        recommended = sorted(data.items(), key=lambda x: x[1], reverse=True)[
            0][0] == "first"
        recommended_str = "Recommended" if recommended else ""
        performance = "%.2f %%" % data["first"]
        color = "primary" if recommended else "secondary"
        textColor = "text-white" if recommended else "text-primary"
        return recommended_str, performance, color, textColor

    
    @app.callback(
        [
            Output("second-recommended", "children"),
            Output("second-proba", "children"),
            Output("second-header", "color"),
            Output("second-header", "className"),
        ],
        [
            Input("major-data", "children")
        ]
    )
    def render_second_title(data: str) -> (str, str, str, str):
        """
        Used for rendering the GUI element of the second major choice
        """
        if not data:
            return "", "", "", ""

        data = json.loads(data)
        recommended = sorted(data.items(), key=lambda x: x[1], reverse=True)[
            0][0] == "second"
        recommended_str = "Recommended" if recommended else ""
        performance = "%.2f %%" % data["second"]
        color = "primary" if recommended else "secondary"
        textColor = "text-white" if recommended else "text-primary"
        return recommended_str, performance, color, textColor

    
    @app.callback(
        [
            Output("third-recommended", "children"),
            Output("third-proba", "children"),
            Output("third-header", "color"),
            Output("third-header", "className"),
        ],
        [
            Input("major-data", "children")
        ]
    )
    def render_third_title(data: str) -> (str, str, str, str):
        """
        Used for rendering the GUI element of the third major choice
        """
        if not data:
            return "", "", "", ""

        data = json.loads(data)
        recommended = sorted(data.items(), key=lambda x: x[1], reverse=True)[
            0][0] == "third"
        recommended_str = "Recommended" if recommended else ""
        performance = "%.2f %%" % data["third"]
        color = "primary" if recommended else "secondary"
        textColor = "text-white" if recommended else "text-primary"
        return recommended_str, performance, color, textColor