import pandas as pd
import numpy as np
import math
import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot
import matplotlib.pyplot as plt
import plotly.plotly as py
init_notebook_mode(connected=True)

def get_grouped():
    BA_job = pd.read_csv('BA_job_clean.csv')
    Grouped_BA = BA_job.groupby('State')
    Grouped_df = Grouped_BA.describe()
    return Grouped_df

def get_barplot_salaryrange():
    Grouped_df = get_grouped()
    state_name = Grouped_df.index.get_values()
    lower = Grouped_df['Salary_Lower_Bound']['mean']
    upper = Grouped_df['Salary_Upper_Bound']['mean']
    trace1 = go.Bar(
                    x = state_name,
                    y = lower,
                    name='Lower Salary',
                    width = 0.8,
                    text = lower.round(0),
                    textposition = 'auto'     
                    )
    trace2 = go.Bar(
                    x = state_name,
                    y = upper,
                    name='Upper Salary',
                    width = 0.8,
                    text = upper.round(0),
                    textposition = 'auto'
                    )

    data = [trace1, trace2]
    layout = go.Layout(title = 'Upper and Lower Range Salary for Business Analyst Positions by States',
                       barmode='stack',
                       xaxis = dict(
                                   title = 'State Name',
                                   ticklen = 5,
                                   zeroline = False,
                                   gridwidth = 2,
                                   ),
                       yaxis = dict(
                                   title = 'Salary (in thousands)',
                                   ticklen = 5,
                                   gridwidth = 2,
                                   ),
                        )

    fig = go.Figure(data=data, layout=layout)
    return py.plot(fig, filename='stacked-bar')
    