#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[3]:


df= pd.read_csv ("E:\StudentsPerformance.csv")


# In[5]:


df.head(20)


# In[6]:


df.tail()


# In[7]:


df.info()


# In[8]:


df.describe()


# In[10]:


df.interpolate(method='linear')


# In[11]:


df.info()


# In[15]:


sns.boxplot(x='math score', y='reading score' , data=df)


# In[16]:


p = sns.countplot(x="math score", data = df, palette="muted")
_ = plt.setp(p.get_xticklabels(), rotation=90) 


# In[25]:


print (df.shape)


# In[26]:


sns.countplot(x="reading score", data = df, palette="muted")
plt.show()


# In[29]:


df.isnull().sum()


# In[ ]:




