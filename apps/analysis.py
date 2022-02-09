import dash
from dash import dcc, html, callback_context
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go




layout = html.Div([
    
    dbc.Row([
        html.Div([
            html.H2('Wine Data analysis'),
            ], className='analysis-title'),
        
        ], className='analysis-row1'),
    
    dbc.Row([
        dbc.Col([
            html.Div([
                html.P("This project is a follow-up to a data analysis course."),
                html.P("The data used comes from a dataset of French and Italian wines and from scraping of specialized websites."),
                html.P("The preprocessing was coded in Python, the NLP part was done with Sklearn and the application with Dash. The code is available on Github."),
                dcc.Link(dbc.Button('Github', id='github-btn'), href='#', target="_blank"),
                ], className='tableau-txt'),
            ], className='analy-col1'),
        
        dbc.Col([
            html.Div([
                html.P("I've made an analysis of a wine dataset for the Wild Code School final checkpoint."),
                html.P("This analysis has been made with Tableau Software."),
                html.P("If you want to see it, it's simple : click on the button and enjoy !"),
                dcc.Link(dbc.Button('Tableau dashboard', id='tableau-btn'), href='https://public.tableau.com/app/profile/alexandra.houssin/viz/Wineanalysis_16443073631540/Prsentation?publish=yes', target="_blank"),
                ], className='tableau-txt'),
            ], className='analy-col2')
        
        ],className= 'analysis-row2')
    
], className = 'analysis-content')