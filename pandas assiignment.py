#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[59]:


import numpy as np


# In[9]:


df = pd.read_csv("./desktop/data/vgsales.csv")
df.head(10)


# In[5]:


df.shape


# In[6]:


df.describe()


# In[8]:


type(df)


# In[3]:


games = pd.read_csv("./desktop/data/vgsales.csv")
games.head(10)


# In[10]:


#Number 5
grouped_df = df.groupby('Global_Sales')['Name']
grouped_df.head(5)


# In[70]:


grouped_df = df.groupby("NA_Sales")["Genre"].sum()
grouped_df


# In[72]:


grouped_df = df.groupby("Publisher")["Global_Sales"].count()
grouped_df


# In[ ]:




