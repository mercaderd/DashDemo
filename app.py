# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

df_global_confirmed = pd.read_csv('./confirmed_data.csv', index_col=0)
df_global_deaths = pd.read_csv('./deaths_data.csv', index_col=0)
df_eu_confirmed = pd.read_csv('./confirmed_eu_data.csv', index_col=0)
df_eu_deaths = pd.read_csv('./deaths_eu_data.csv', index_col=0)

tr_global_confirmed = [go.Scatter(x=df_global_confirmed.index, y=df_global_confirmed[s].values, name=s, mode='lines+markers') for s in df_global_confirmed.columns]
tr_global_deaths = [go.Scatter(x=df_global_deaths.index, y=df_global_deaths[s].values, name=s, mode='lines+markers') for s in df_global_deaths.columns]
tr_eu_confirmed = [go.Scatter(x=df_eu_confirmed.index, y=df_eu_confirmed[s].values, name=s, mode='lines+markers') for s in df_eu_confirmed.columns]
tr_eu_deaths = [go.Scatter(x=df_eu_deaths.index, y=df_eu_deaths[s].values, name=s, mode='lines+markers') for s in df_eu_deaths.columns]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    html.H1(children='Covid-19 Dash'),

    html.Div(children='''
        Daily updated Covid-19 data
    '''),

    dcc.Graph(
        id='global-confirmed',
        figure={
            'data': tr_global_confirmed,
            'layout': {
                'title': 'Covid-19 EU-USA Confirmed',
                'yaxis': {'type': 'log'}

            }
        }
    ),

dcc.Graph(
        id='global-deaths',
        figure={
            'data': tr_global_deaths,
            'layout': {
                'title': 'Covid-19 EU-USA Deaths',
                'yaxis': {'type': 'log'}

            }
        }
    ),

dcc.Graph(
        id='eu-confirmed',
        figure={
            'data': tr_eu_confirmed,
            'layout': {
                'title': 'Covid-19 EU Confirmed',
                'yaxis': {'type': 'log'}

            }
        }
    ),

dcc.Graph(
        id='eu-deaths',
        figure={
            'data': tr_eu_deaths,
            'layout': {
                'title': 'Covid-19 EU Deaths',
                'yaxis': {'type': 'log'}

            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)