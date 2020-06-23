### Data
import pandas as pd
import pickle
### Graphing
import plotly.graph_objects as go
### Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
## Navbar
from navbar import Navbar
df = pd.read_csv('/var/www/html/data_score/google_search_Achin.csv')
df.set_index(df.iloc[:,0], drop = True, inplace = True)
df = df.iloc[:,1:]

nav = Navbar()

header = html.H3(
    'Select the name of the metrics to get the score'
)

options = [{'label':x.replace(', Illinois', ''), 'value': x} for x in df.columns]

dropdown = html.Div(dcc.Dropdown(
    id = 'pop_dropdown',
    options = options,
    value = 'Introvert'
))

output = html.Div(id = 'output',
                children = [],
                )
text=html.Div(
        html.H1(
            
            ))

def App():
    layout = html.Div([
        nav,
        header,
        dropdown,
        output
    ])
    return layout

def build_graph(city):
    data = [go.Scatter(x = df.index,
                        y = df[city],
                        marker = {'color': 'orange'})]
    graph = dcc.Graph(
           figure = {
               'data': data,
               'layout': go.Layout(
                    title = '{} '.format(city).upper(),
                    yaxis = {'title': 'Score'},
                    xaxis={'title':"Timeline"},
                    hovermode = 'closest'
                                  )
                       }
             )
    return graph

