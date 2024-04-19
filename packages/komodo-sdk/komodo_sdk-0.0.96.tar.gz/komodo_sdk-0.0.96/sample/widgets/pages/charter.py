import dash
import dash_bootstrap_components as dbc
import dash_chart_editor as dce
import pandas as pd
from dash import html

dash.register_page(__name__)


def layout():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
    return html.Div([
        html.H4("Dash Chart Editor Demo with the Plotly Solar dataset"),
        html.Br(),
        dbc.Row([
            dbc.Col(dce.DashChartEditor(dataSources=df.to_dict("list")), width=6, className="grid-padding"),
            dbc.Col(dce.DashChartEditor(dataSources=df.to_dict("list")), width=6, className="grid-padding")
        ]),
        dbc.Row([
            dbc.Col(dce.DashChartEditor(dataSources=df.to_dict("list")), width=6, className="grid-padding"),
            dbc.Col(dce.DashChartEditor(dataSources=df.to_dict("list")), width=6, className="grid-padding")
        ])
    ])
