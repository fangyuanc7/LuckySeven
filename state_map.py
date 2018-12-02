import pandas as pd
import numpy as np
from plotly.offline import init_notebook_mode,iplot
import plotly.plotly as py
import plotly.tools as tls
init_notebook_mode(connected=True) 
tls.set_credentials_file(username = 'shmylm', api_key = 'rJXTWcMKPD4xWVrXqF1W')

# Create a dataframe which will contains two columns: state and counts(number of positions in each state)
def get_state_dataframe():
    BA_job = pd.read_csv('BA_job_clean.csv') 
    state_dict = {}
    state = []
    counts = []
    for i in range(len(BA_job)):
        if BA_job['State'][i] not in state_dict:
            state_dict[BA_job['State'][i]] = 1
        else:
            state_dict[BA_job['State'][i]] += 1     
    for i in state_dict.keys():
        state.append(i)
    for i in state_dict.values():
        counts.append(i)
    state = pd.DataFrame({'State':state, 'Counts':counts})
    return state

def get_graph():
    state = get_state_dataframe()
    state['text'] = 'State ' + state['State'].astype(str) + '<br>' + 'Counts ' + state['Counts'].astype(str)
    data = [dict(type = 'choropleth', locations = state['State'], 
                 z = state['Counts'], locationmode = 'USA-states',
                 text = state['text'], colorscale = 'JET', 
                 colorbar = dict(title = 'Number of Positions'))]
    layout = dict(title = "US Business Analyst Positions by States", 
                  geo = dict(scope='usa', projection = dict(type = "albers usa")))
    fig = dict(data = data, layout = layout)
    return py.plot(fig, filename = "BA_Positions-choropleth.map")