# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('./confirmed_data.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='y-time-series',
        figure={
            'data': [go.Scatter(x=df['X'], y=df['EU'], name='EU'),go.Scatter(x=df['X'], y=df['US'], name='US')]
            ,
            'layout': {
                'title': 'Covid-19 Confirmed',
                'yaxis': {'type': 'log'}

            }
        }
    ),

dcc.Graph(
        id='x-time-series',
        figure={
            'data': [
                {'x': ['1/2/2020', '2/2/2020', '3/2/2020'], 'y': [10, 100, 1000],  'name': 'SF'},
                {'x': ['1/2/2020', '2/2/2020', '3/2/2020'], 'y': [2, 400, 980],  'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Covid-19 Deaths',
                'yaxis': {'type': 'log'}

            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)