import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
#By Dev Patel from FTC Team Robot Uprising 14607

from utils import Header, make_dash_table


import pathlib
import pandas as pd
# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_team_facts = pd.read_csv(DATA_PATH.joinpath("team_facts.csv"))
#file name says df_price_per.csv but it just contains a bunch of sample
#data and stuff like that uwu :)
df_time = pd.read_csv(DATA_PATH.joinpath("sample_data.csv")).time
df_M1C = pd.read_csv(DATA_PATH.joinpath("sample_data.csv")).M1C
df_M2C = pd.read_csv(DATA_PATH.joinpath("sample_data.csv")).M2C
df_M1P = pd.read_csv(DATA_PATH.joinpath("sample_data.csv")).M1P
df_M2P = pd.read_csv(DATA_PATH.joinpath("sample_data.csv")).M2P
def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # Main Page
            html.Div(
                [
                    # Row 3 (Main Title and Info)
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Alpha Stage Version 0.1"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                    Welcome to the FTC Log Analyzer! This app is a simple, lightweight \
                                    app aimed to help FTC Teams visualize REV Hub Data. The REV Hub is the \
                                    premier choice in electronics hubs for FTC Teams, and it's abundant array  \
                                    ports and sensors allow for Teams to have programmatic access to metrics \
                                    collected from their robot. However, a challenge many teams face is being \
                                    able to effectively visualize said metrics. The Log Analyzer uses Plot.ly \
                                    and Dash, and can be downloaded an ran locally in environments without Wifi. \
                                    ",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4 (Quick Table) and Position Graph
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Team Facts"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_team_facts)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Motor Position",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        figure=dict(
                                            data=[
                                                dict(
                                                    x= df_time,
                                                    y= df_M1P,
                                                    name='Motor 1 Position',
                                                    marker=dict(
                                                        color='rgb(55, 83, 109)'
                                                    )
                                                ),
                                                dict(
                                                    x= df_time,
                                                    y= df_M2P,
                                                    name='Motor 2 Position',
                                                    marker=dict(
                                                        color='rgb(26, 118, 255)'
                                                    )
                                                )
                                                
                                            ],
                                            layout=dict(
                                                title='Motor Position vs Time of Motor 1 and 2',
                                                showlegend=True,
                                                legend=dict(
                                                    x=0,
                                                    y=1.0
                                                ),
                                                margin={
                                                    "r": 30,
                                                    "t": 30,
                                                    "b": 30,
                                                    "l": 30,
                                                },                                            )
                                        ),
                                        style={'height': 300},
                                        id='my-graph'
                                    )  
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 5 (Current Graph)
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Current Draw",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        figure=dict(
                                            data=[
                                                dict(
                                                    x= df_time,
                                                    y= df_M1C,
                                                    name='Motor 1 Current',
                                                    marker=dict(
                                                        color='rgb(55, 83, 9)'
                                                    )
                                                ),
                                                dict(
                                                    x= df_time,
                                                    y= df_M2C,
                                                    name='Motor 2 Current',
                                                    marker=dict(
                                                        color='rgb(26, 118, 255)'
                                                    )
                                                )
                                                
                                            ],
                                            layout=dict(
                                                title='Motor Current vs Time of Motor 1 and 2',
                                                showlegend=True,
                                                legend=dict(
                                                    x=0,
                                                    y=1.0
                                                ),
                                                margin={
                                                    "r": 30,
                                                    "t": 30,
                                                    "b": 30,
                                                    "l": 30,
                                                }, 
                                            )
                                        ),
                                        style={'height': 300},
                                        id='my-graph'
                                    )  
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                ])
        ],
        className="page",)