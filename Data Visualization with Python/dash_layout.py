# Import required packages
import pandas as pd 
import dash
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.express as px
from dash.dependencies import Input, Output

# Add Dataframe

# Add a bar graph figure

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Dashboard', style={'textAlign': 'center'}

    )
    # Create dropdown,

    # Create dropdown
    dcc.Dropdown(options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': u'MontrÃ©al', 'value': 'MTL'}, 
        {'lable': 'San Francisco', 'value': 'SF'}
    ], value='NYC' # Providing a value to dropdown

    )

    # Bar graph
])

# Run Application
if __name__ == '__main__':
    app.run_server()
