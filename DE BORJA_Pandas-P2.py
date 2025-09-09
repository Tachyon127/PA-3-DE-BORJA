#!/usr/bin/env python
# coding: utf-8

# #### Problem 2

# In[3]:


import pandas as pd
cars = pd.read_csv('cars.csv')


# In[4]:


cars.iloc[:5, ::2]


# In[5]:


cars.loc[cars['Model']=='Mazda RX4']


# In[6]:


cars.loc[cars['Model']=='Camaro Z28', ['cyl']]


# In[7]:


cars_model = ['Mazda RX4', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(cars_model), ['cyl', 'gear']]

