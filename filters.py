import numpy as np
import pandas as pd
import ast

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, Select, TextInput
from bokeh.plotting import figure, output_file, show
from bokeh.models.widgets import RangeSlider, Button, DataTable, TableColumn, NumberFormatter
from os.path import dirname, join


data = pd.read_csv('BA_job_clean.csv')


salary_slider = Slider(title="Minimum annul salary (in thousands)", start=0, end=200, value=10, step=1)
salary_slider.on_change('value', lambda attr, old, new: update())

city = Select(title="Location", value="All", options=open('city.txt').read().split('\n'))
city.on_change('value', lambda attr, old, new: update())

company = Select(title="Company", value="All", options=open('company.txt').read().split('\n'))
company.on_change('value', lambda attr, old, new: update())

keyword = TextInput(title="Keywords")
keyword.on_change('value', lambda attr, old, new: update())


def select_jobs():
    company_val = str(company.value)
    city_val = str(city.value)
    kwd_val = str(keyword.value)
    
    selected = data[data.Salary_Upper_Bound >= salary_slider.value]
    
    if (company_val != "All"):
        selected = selected[selected.Company.str.contains(company_val) == True]
    if (city_val != "All"):
        selected = selected[selected.City.str.contains(city_val) == True]
    if (keyword != ""):
        selected = selected[selected.Description.str.contains(kwd_val) == True]
    return selected


def update():
    current = select_jobs()
    source.data = current.to_dict('list') 



source = ColumnDataSource(data=dict())

columns = [
    TableColumn(field="Name", title="Name"),
    TableColumn(field="Salary", title="Salary"),
    TableColumn(field="City", title="City"),
    TableColumn(field="Company", title="Company"),
    TableColumn(field="Description", title="Description")
] 




data_table = DataTable(source=source, columns=columns, width=800)

controls = widgetbox(salary_slider,city,company,keyword)
table = widgetbox(data_table)


curdoc().add_root(row(controls,table))
curdoc().title = "TEST Tools Project"

update()

