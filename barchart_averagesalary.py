import pandas as pd
import numpy as np
import math
import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot
import matplotlib.pyplot as plt
import plotly.plotly as py

init_notebook_mode(connected=True)

# Creat two lists named Lower_Salary and Upper_Salary, which corresponding to the Salary_Lower_Bound 
# and Salary_Upper_Bound columns in the cleaned dataframe. Append value 0 to the list if the data is missing
# Add one column named Average_Salary to cleanned dataset then geted a dataframe grouped by State

def get_grouped_dataframe():
    BA_job = pd.read_csv('BA_job_clean.csv')
    Lower_Salary = []
    Upper_Salary = []
    Average_Salary = []
    for i in range(len(BA_job)):
        if math.isnan(BA_job['Salary_Lower_Bound'][i]) == True:
            Lower_Salary.append(0)
        else:
            Lower_Salary.append(int(BA_job['Salary_Lower_Bound'][i]))
    for i in range(len(BA_job)):
        if math.isnan(BA_job['Salary_Upper_Bound'][i]) == True:
            Upper_Salary.append(0)
        else:
            Upper_Salary.append(int(BA_job['Salary_Upper_Bound'][i]))
    
    for i in range(len(Lower_Salary)):
        Average_Salary.append((Lower_Salary[i] + Upper_Salary[i])/2)
    BA_job['Average_Salary'] = Average_Salary
    Grouped_BA = BA_job.groupby('State')
    Grouped_df = Grouped_BA.describe()
    return Grouped_df

def get_barplot_average_salary():
    Grouped_df=get_grouped_dataframe()
    State_name = Grouped_df.index.get_values()
    Average_Mean = Grouped_df['Average_Salary']['mean']
    data = [go.Bar(
        x = State_name,
        y = Average_Mean,
        width = 1,
        text = Average_Mean.round(0),
        textposition = 'auto',
        marker = dict(
        color = 'rgb(158,202,225)',
        line = dict(
        color = 'rgb(8,48,107)',
        width = 1.5),
        opacity = 0.6,
       ))]
    layout = dict(title = 'Average Salary for Business Analyst Positions in Different States',
             xaxis = dict(
             title = 'State Name',
             ticklen = 5,
             zeroline = False,
             gridwidth = 2,
             ),
             yaxis = dict(
             title = 'Average_Salary (in thousands)',
             ticklen = 5,
             gridwidth = 2,
             ),)

    fig = go.Figure(data = data, layout = layout)
    return py.plot(fig, filename = 'basic-bar')