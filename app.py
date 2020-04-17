# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    html.H1(id='title', children='Covid-19 Dash'),
    html.Button('Update', id='update-plots', n_clicks=0),
    html.Div(children=[

        html.H3('Global Data', style={'text-align': 'center'}),
        html.Div(children = [
            dcc.Graph(
                    id='global-confirmed'
                ),

            dcc.Graph(
                    id='global-deaths'
                )
            ]),

        html.H3('EU Data', style={'text-align': 'center'}),
        html.Div([
            dcc.Graph(
                    id='eu-confirmed'
                ),

            dcc.Graph(
                    id='eu-deaths'
                )
        ])
    ], style={'columnCount': 2})
])

@app.callback(
    dash.dependencies.Output('global-confirmed', 'figure'),
    [dash.dependencies.Input('update-plots', 'n_clicks')])
def update_plot1(n_clicks):
    url = 'https://github.com/mercaderd/python-notebooks/raw/master/covid_data_csv/confirmed_data.csv'
    df = pd.read_csv(url, index_col=0)
    tr = [
        go.Scatter(x=df.index, y=df[s].values, name=s, mode='lines') for s in
        df.columns]
    return {
                'data': tr,
                'layout': {
                    'title': 'Covid-19 EU-USA Confirmed',
                    'yaxis': {'type': 'log'}

                }
    }

@app.callback(
    dash.dependencies.Output('global-deaths', 'figure'),
    [dash.dependencies.Input('update-plots', 'n_clicks')])
def update_plot2(n_clicks):
    url = 'https://github.com/mercaderd/python-notebooks/raw/master/covid_data_csv/deaths_data.csv'
    df = pd.read_csv(url, index_col=0)
    tr = [
        go.Scatter(x=df.index, y=df[s].values, name=s, mode='lines') for s in
        df.columns]
    return {
                'data': tr,
                'layout': {
                    'title': 'Covid-19 EU-USA Deaths',
                    'yaxis': {'type': 'log'}

                }
    }

@app.callback(
    dash.dependencies.Output('eu-confirmed', 'figure'),
    [dash.dependencies.Input('update-plots', 'n_clicks')])
def update_plot3(n_clicks):
    url = 'https://github.com/mercaderd/python-notebooks/raw/master/covid_data_csv/confirmed_eu_data.csv'
    df = pd.read_csv(url, index_col=0)
    tr = [
        go.Scatter(x=df.index, y=df[s].values, name=s, mode='lines') for s in
        df.columns]
    return {
                'data': tr,
                'layout': {
                    'title': 'Covid-19 EU Confirmed',
                    'yaxis': {'type': 'log'}

                }
    }

@app.callback(
    dash.dependencies.Output('eu-deaths', 'figure'),
    [dash.dependencies.Input('update-plots', 'n_clicks')])
def update_plot4(n_clicks):
    url = 'https://github.com/mercaderd/python-notebooks/raw/master/covid_data_csv/deaths_eu_data.csv'
    df = pd.read_csv(url, index_col=0)
    tr = [
        go.Scatter(x=df.index, y=df[s].values, name=s, mode='lines') for s in
        df.columns]
    return {
                'data': tr,
                'layout': {
                    'title': 'Covid-19 EU Deaths',
                    'yaxis': {'type': 'log'}

                }
    }

if __name__ == '__main__':
    app.run_server(debug=True)