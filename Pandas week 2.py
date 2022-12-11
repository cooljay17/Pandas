#!/usr/bin/env python
# coding: utf-8

# # Data in Motion Pandas Week 2 challenge

# In[ ]:


import pandas as pd
import numpy as np


# In[2]:


print(pd.__version__)


# Read the CSV file

# In[6]:


data = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv', sep=',')


# Count the number of Teams

# In[15]:


data['Team'].count()


# Count the number of Columns

# In[16]:


data.shape


# In[17]:


data.head(1)


# View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline.

# In[24]:


discipline=data[['Team','Yellow Cards','Red Cards']]


# In[25]:


print(discipline)


# Sort the teams by Red Cards, then to Yellow Cards.

# In[26]:


discipline.sort_values(['Red Cards','Yellow Cards'])


# Calculate the mean Yellow Cards given per Team.

# In[54]:


#discipline['Yellow Cards'].mean()
data.groupby('Team')['Yellow Cards'].mean()


# Filter teams that scored more than 6 goals.

# In[28]:


data[data['Goals'] > 6]


# Select the teams that start with the letter G

# In[39]:


data[data['Team'].str.startswith('G')]


# Select the first 7 columns.

# In[40]:


data.iloc[: , :7]


# Select all columns except the last 3.

# In[41]:


data.loc[:, ~data.columns.isin(['Subs on','Subs off','Players Used'])]


# Present only the Shooting Accuracy from England, Italy and Russia.

# In[53]:


data.loc[data['Team'].isin(['England','Italy','Russia']),'Shooting Accuracy']
          
           


# In[ ]:




