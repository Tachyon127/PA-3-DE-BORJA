#!/usr/bin/env python
# coding: utf-8

# #### Problem 2

# In[49]:


import pandas as pd
cars = pd.read_csv('cars.csv')
cars


# In[48]:


cars.iloc[:5, ::2]


# In[24]:


cars.loc[cars['Model']=='Mazda RX4']


# In[25]:


cars.loc[cars['Model']=='Camaro Z28', ['cyl']]


# In[38]:


cars_model = ['Mazda RX4', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(cars_model), ['cyl', 'gear']]

