#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv('/Users/deion/TweetsByLocation/covid19_tweets.csv')


# In[5]:


df.info()


# In[6]:


df.describe()


# In[9]:


df.isnull().count()


# In[10]:


df = df.dropna()


# In[12]:


pd.DatetimeIndex(df['date']).month.unique()


# In[13]:


top_july = df['user_location'][pd.DatetimeIndex(df['date']).month == 7].value_counts()
top_august = df['user_location'][pd.DatetimeIndex(df['date']).month == 8].value_counts()
top_all_the_time = (top_august + top_july).sort_values(ascending = False)
print(top_all_the_time)

# In[16]:


fig, ax = plt.subplots(figsize = (13,5))
plt.xlabel("Location", fontsize = 12)
plt.ylabel("NO. Tweets", fontsize = 12)
top_all_the_time[0:15].plot(kind='bar', title = "Top 15 Countries Posting about Covid-19", )


# In[17]:


# In[18]:





# In[ ]:




