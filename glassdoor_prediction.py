# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('glassdoor_jobs.csv')

# Salary col remove -1
df=df[df['Salary Estimate'] != '-1']

# Create new col for hour
df['hourly']=df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

# create sepereate col for emp estimator
df['employer_provided']  = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

# remove est salary keyword
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])


# REmove $ and k
minus_kd = salary.apply(lambda x:x.replace('K','').replace('$',''))

# remove emp provided salary  and per hour
minus_hr_eps = minus_kd.apply(lambda x:x.lower().replace('per hour','').replace('employer provided salary:',''))

# split min and max sal range
df['min_sal']=minus_hr_eps.apply(lambda x: int(x.split('-')[0]))
df['max_sal']=minus_hr_eps.apply(lambda x: int(x.split('-')[1]))


# clean company col

df['company_name']= df.apply(lambda x:x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis=1)

# Seperate state from location column
df['job_state']=df['Location'].apply(lambda x: x.split(',')[1])

# Take details from description column
df['python_yn']=df['Job Description'].apply(lambda x:1 if 'python' in x.lower() else 0)

df['R_yn']=df['Job Description'].apply(lambda x:1 if 'r-studio' in x.lower() or  'r studio' in x.lower() or  ' r ' in x.lower() else 0)

df['spark_yn']=df['Job Description'].apply(lambda x:1 if 'spark' in x.lower() else 0)

df['aws_yn']=df['Job Description'].apply(lambda x:1 if 'aws' in x.lower() else 0)

df['excel_yn']=df['Job Description'].apply(lambda x:1 if 'excel' in x.lower() or  'ms_excel' in x.lower() else 0)


# Age of the company

df['company_age']= df['Founded'].apply(lambda x: 1 if x<0 else int(2020-x))

# drop unnamed col
df.drop(['Unnamed: 0'], axis =1, inplace=True)

# export df to excel
df.to_csv('Salary_glassdoor_cleaned.csv', index=False)






























































