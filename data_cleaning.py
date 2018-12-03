import pandas as pd
import numpy as np
import math

def modify_data():
    BA_job = pd.read_csv('BA_job.csv')
    for i in range(len(BA_job['Salary'])):
        if type(BA_job['Salary'][i]) != str:
            if math.isnan(BA_job['Salary'][i]) == True:
                BA_job['Salary'][i] = BA_job['Salary'][i]
        elif 'per hour' not in BA_job['Salary'][i]:
            BA_job['Salary'][i] = BA_job['Salary'][i]
        elif 'per hour' in BA_job['Salary'][i]:
            l = int(int(BA_job['Salary'][i][1:3])*40*4*12/1000)
            u = int(int(BA_job['Salary'][i][5:7])*40*4*12/1000)
            BA_job['Salary'][i] = '$' + str(l) + 'k' + '-' + '$' + str(u) + 'k'
    return BA_job   

def get_range():
    BA_job_data = modify_data()
    lower = []
    upper = []
    for i in range(len(BA_job_data['Salary'])):
        if type(BA_job_data['Salary'][i]) != str:
            if math.isnan(BA_job_data['Salary'][i]) == True:
                lower.append(None)
                upper.append(None)
        else:
            salary = BA_job_data['Salary'][i]
            salary = salary.split('k')
            lower.append(salary[0][1:])
            upper.append(salary[1][2:])
    return lower, upper

def get_cleaned_dataset():
    BA_job_data = modify_data()
    BA_job_data['Salary_Lower_Bound'] = get_range()[0]
    BA_job_data['Salary_Upper_Bound'] = get_range()[1]
    city_set = pd.read_csv('city_sets.csv')
    city_list = list(city_set["City Name"])
    BA_job_data = BA_job_data[BA_job_data['City'].isin(city_list)]
    BA_job_data = BA_job_data.reset_index(drop=True)
    BA_job_data.to_csv('BA_job_clean.csv', header=True, index=False)