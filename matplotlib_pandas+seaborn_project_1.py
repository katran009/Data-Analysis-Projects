#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')


# In[2]:


tips.head()


# In[3]:


iris.head()


# 1. Matplotlib example below:

# In[11]:


dates = [
    '1981-01-01', '1981-01-02', '1981-01-03', '1981-01-04', '1981-01-05',
    '1981-01-06', '1981-01-07', '1981-01-08', '1981-01-09', '1981-01-10'
]
min_temperature = [20.7, 17.9, 18.8, 14.6, 15.8, 15.8, 15.8, 17.4, 21.8, 20.0]
max_temperature = [34.7, 28.9, 31.8, 25.6, 28.8, 21.8, 22.8, 28.4, 30.8, 32.0]

fig,axes = plt.subplots(nrows=1, ncols=1, figsize=(15,10))
axes.plot(dates, min_temperature, label='Min Temperature')
axes.plot(dates, max_temperature, label = 'Max Temperature')
axes.legend()


# 2. Seaborn example below:

# In[13]:


Relational Plots
  scatterplot()
  lineplot()
Categorical Plots
  striplot()    swarmplot()
  boxplot()     boxenplot()
  violinplot()  countplot()
  pointplot()   barplot()
Distribution Plots
  distplot()
  kdeplot()
  rugplot()
Regression Plots
  regplot()
  residplot()
MatrixPlots()
  heatmap()


# In[16]:


sns.scatterplot(x='total_bill',y='tip', data=tips, s=50)


# In[19]:


row_variable = 'day'
col_variable = 'smoker'
hue_variable = 'sex'
row_variables = tips[row_variable].unique()
col_variables = tips[col_variable].unique()
num_rows = row_variables.shape[0]
num_cols = col_variables.shape[0]

fig,axes = plt.subplots(num_rows, num_cols, sharex=True, sharey=True, figsize=(15,10))
subset = tips.groupby([row_variable,col_variable])
for row in range(num_rows):
    for col in range(num_cols):
        ax = axes[row][col]
        row_id = row_variables[row]
        col_id = col_variables[col]
        ax_data = subset.get_group((row_id, col_id))
        sns.scatterplot(x='total_bill', y='tip', data=ax_data, hue=hue_variable,ax=ax)
        title = row_variable + ' : '  + row_id + ' ' + col_variable + ' : ' + col_id
        ax.set_title(title)


# In[20]:


grid = sns.catplot(x='sex', y='total_bill', col='day', col_wrap=2, hue='smoker', data=tips, kind='box', height=4, aspect=1.5)


# In[21]:


grid = sns.lmplot(x='total_bill', y='tip', col='day', col_wrap=3, hue='sex', data=tips)


# In[22]:


row_variables = iris.columns[:-1]
column_variables = iris.columns[:-1]
num_rows = row_variables.shape[0]
num_columns = column_variables.shape[0]
fig,axes = plt.subplots(num_rows, num_columns, sharey=True)
for i in range(num_rows):
    for j in range(num_columns):
        ax = axes[i][j]
        row_variable = row_variables[i]
        column_variable = column_variables[j]
        sns.scatterplot(x=column_variable, y=row_variable, data=iris, ax=ax)


# In[23]:


pairgrid = sns.PairGrid(data=iris)
pairgrid = pairgrid.map_offdiag(sns.scatterplot)
pairgrid = pairgrid.map_diag(plt.hist)


# In[ ]:




