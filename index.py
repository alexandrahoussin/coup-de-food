import dash
from dash import dcc, html, callback_context
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go

# connect to main app.py & other pages
from app import app
from apps import reco, analysis

#------------------- Item -----------------------------------

sidebar = html.Header([
    html.Div([html.Img(src='assets/logo.png', className='logo-img'),], className="logo"),
    html.Div([
        dbc.Nav(
            [                
                dbc.NavLink("Home  |", href="/", active="exact"),
                dbc.NavLink('Wine & Food Love Machine  |', href="/apps/reco", active="exact"),
                dbc.NavLink('Wine Data Analysis', href="/apps/analysis", active="exact"),
                
              
            ],
            className= 'navlink'
        ),
        ], className='header-links')
], className= 'sidebar')

content = html.Div(id='page-content', className='page-content')

page = html.Div([
    dbc.Row([
        
        dbc.Col([
            html.Div([
                html.H1("Coup de Food"),
                html.P("Finding the perfect match between a dish and a wine... like in love, it is not easy. \
                    What are our criteria, the qualities we are looking for in a wine? When will I drink it? With which dish? \
                    When we eat, the wine must have its aromas exalted. But each person has his own sensitivities, his own tastes.That's why Coup de Food helps you find the perfect match between a dish and a wine, according to your tastes. But if this match does not exist on paper, Coup de Food will suggest alternatives and you can test your affinities." 
                , className="project-info"),
                dcc.Link(dbc.Button('GET STARTED', id='get-started'), href='/apps/reco'),
                ], className='project-title'),
            ], width=5, className='text-col'),
        
        dbc.Col([
            html.Div([
                html.Img(src='assets/date.png', className='home-img'),
                ], className="img-cont")
            ], className='img-col'),
        
        ], className='row1')
    
    ], className='content')


#------------------- LAYOUT -----------------------------------
app.layout = html.Div([
    dcc.Location(id='url'),
    sidebar, 
    content])

#------------------- Callbacks -----------------------------------
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == '/':
        return page
    if pathname == "/apps/analysis":
        return analysis.layout
    if pathname == "/apps/reco":
        return reco.layout
    

if __name__=='__main__':
    app.run_server(debug=True)