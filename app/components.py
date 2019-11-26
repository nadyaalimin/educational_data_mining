from random import randint

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pickle


curr_course_list = {
    'Science': [
        ('phy', 'Physics'),
        ('chem', 'Chemistry'),
        ('bio', 'Biology'),
    ],
    'Social': [
        ('econ', 'Economy'),
        ('geo', 'Geography'),
        ('soc', 'Sociology'),
    ],
    'General': [
        ('eng', 'English'),
        ('math', 'Mathematics'),
        ('fin', 'Final National Exam'),
    ],
}


major_le_dict = pickle.load(open("app/data/major_le_dict.pkl", 'rb'))
major_options = [{'label':major, 'value':code} for major,code in major_le_dict.items()]
major_options.insert(0, {'label': '-', 'value': -1})
major_choice_list = {
    'first': 'First Choice',
    'second': 'Second Choice',
    'third': 'Third Choice'
}


class Header:
    @staticmethod
    def render():
        element = [
            dbc.Row([
                dbc.Col([
                    html.H1("Pelita Harapan Major Recommender System"),
                    html.P(
                        "Input your high school data below and find the most suitable major for you at Universitas Pelita Harapan!")
                ])
            ],
                className="mt-5"
            )
        ]
        return html.Div(element)


class InputContainer:
    @staticmethod
    def render():
        element = [
            dbc.Row(
                dbc.Col([
                    html.H2("Score Input"),
                    html.P(
                        "Input your average scores from grade 10 to grade 11 for each course. Leave the score 0 for the course you didn't take in high school."
                    )
                ]),
                className="mt-5 mb-2"
            ),
            dbc.Row(
                dbc.Col(
                    [CurrCard.render(curr, courses) for curr, courses in curr_course_list.items()]
                )
            ),
            dbc.Row(
                dbc.Col([
                    html.H2("Major Input"),
                    html.P(
                        "Choose the majors from your top priority to the least priority."
                    )
                ]),
                className="mt-5 mb-2"
            ),
            dbc.Row(
                dbc.Col(
                    [ChoiceInput.render(ch_id, ch_name) for ch_id, ch_name in major_choice_list.items()]
                )
            ),
            dbc.Row(
                dbc.Col(
                    dbc.Button("Show the most fit major for me!",
                               outline=True, color="primary", id="submit-button", className="ml-auto")
                ),
                className="mt-5 mb-5",
            )
        ]
        return html.Div(element)


class CurrCard:
    @staticmethod
    def render(curriculum, courses):
        element = dbc.Card([
            dbc.CardBody([
                html.H4(curriculum, className="card-title text-white mb-0"),
            ]),
            dbc.ListGroup([CourseInput.render(course[0], course[1])
                           for course in courses], flush=True)
        ], color="primary text-primary mt-3")
        return element


class CourseInput:
    @staticmethod
    def render(id, name):
        element = dbc.ListGroupItem([
            name,
            ScoreInput.render(id),
        ], className="d-flex justify-content-between align-items-center")
        return element


class ScoreInput:
    @staticmethod
    def render(id):
        element = dcc.Input(
            type='number',
            min=0,
            max=100,
            id="input-score-" + id,
            value=0
        )
        return element

    
class ChoiceInput:
    @staticmethod
    def render(id, name):
        element = dbc.ListGroupItem([
            name,
            MajorInput.render(id),
        ])
        return element
    
    
class MajorInput:
    @staticmethod
    def render(id):
        element = dcc.Dropdown(
            options=major_options,
            id="input-major-" + id,
            className='dropdown-group',
            clearable=False,
            value=-1
        )
        return element

    
class RecommendationContainer:
    @staticmethod
    def render():
        element = [
            dbc.Row(
                dbc.Col([
                    html.H2("Recommended Major"),
                    html.Span(id="output", className="d-none"),
                    html.Span(id="major-data", className="d-none"),
                ]),
                className="mt-4"
            ),
            OutputContainer.render()
        ]
        return html.Div(element)


class OutputContainer:
    @staticmethod
    def render():
        element = html.Div([
            html.P(
                "Fill up your data and we will try to choose the best major for you!",
                id="output-welcome",
            ),
            dbc.Alert(
                id="output-error",
                color="danger",
                className="d-none",
            ),
            html.Div(
                dbc.CardDeck(
                    [FirstHeader.render(), SecondHeader.render(), ThirdHeader.render()],
                    className="mt-3",
                ),
                id="output-deck",
                className="d-none",
            ),
        ],
            id="output-container"
        )
        return element


class FirstHeader:
    @staticmethod
    def render():
        element = dbc.Card([
            dbc.CardBody([
                html.H4("First Choice",
                        className="card-title"),
                html.Small("Recommended", id="first-recommended",
                           className="card-subtitle"),
            ]),
            dbc.CardFooter([
                "Predicted Success Probability: ",
                html.Span("-", id="first-proba"),
            ], className="border-0"),
        ],
            id="first-header",
            color="primary",
            className="text-white"
        )

        return element


class SecondHeader:
    @staticmethod
    def render():
        element = dbc.Card([
            dbc.CardBody([
                html.H4("Second Choice", className="card-title"),
                html.Small("Recommended", id="second-recommended",
                           className="card-subtitle"),
            ]),
            dbc.CardFooter([
                "Predicted Success Probability: ",
                html.Span("-", id="second-proba"),
            ], className="border-0")
        ],
            id="second-header",
            color="secondary",
            className="text-primary"
        )
        return element


class ThirdHeader:
    @staticmethod
    def render():
        element = dbc.Card([
            dbc.CardBody([
                html.H4("Third Choice", className="card-title"),
                html.Small("Recommended", id="third-recommended",
                           className="card-subtitle"),
            ]),
            dbc.CardFooter([
                "Predicted Success Probability: ",
                html.Span("-", id="third-proba"),
            ], className="border-0")
        ],
            id="third-header",
            color="secondary",
            className="text-primary"
        )
        return element