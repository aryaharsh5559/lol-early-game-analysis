"""
Shared imports and Plotly styling for analysis.ipynb.

Usage:

    from plot_style import *
"""
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from IPython.display import display

# Compact layout used by every chart: centered titles, light grid, tight margins
pio.templates['compact'] = go.layout.Template(
    layout=dict(
        margin=dict(l=30, r=30, t=30, b=30),
        autosize=True,
        width=600,
        height=400,
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        title=dict(x=0.5, xanchor='center'),
    )
)
pio.templates.default = 'simple_white+compact'

pd.set_option('display.max_rows', 7)
pd.set_option('display.max_columns', 8)
pd.set_option('display.precision', 2)


def display_df(df, rows=pd.options.display.max_rows, cols=pd.options.display.max_columns):
    """Display a DataFrame with a given number of rows and columns."""
    with pd.option_context('display.max_rows', rows, 'display.max_columns', cols):
        display(df)
