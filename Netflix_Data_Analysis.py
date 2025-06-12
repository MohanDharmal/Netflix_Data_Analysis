#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('mymoviedb.csv',lineterminator = '\n')


# In[3]:


df


# In[4]:


df.info()


# In[5]:


df.duplicated().sum()


# In[6]:


df.describe()


# In[7]:


df['Release_Date'] = pd.to_datetime(df['Release_Date'])


# In[8]:


print(df['Release_Date'].dtypes)


# In[9]:


df['Release_Date'] = df['Release_Date'].dt.year


# In[10]:


df.head()


# In[11]:


df.drop(columns=['Overview','Original_Language','Poster_Url'],inplace=True)


# In[12]:


df.head()


# In[13]:


df['Genre'].unique()


# In[14]:


df['Popularity'].describe()


# In[15]:


df[df['Popularity']<df['Popularity'].quantile(0.25)]


# In[17]:


def categorize_col(df,col,labels):
    
    edges = [df[col].describe()['min'],
            df[col].describe()['25%'],
            df[col].describe()['50%'],
            df[col].describe()['75%'],
            df[col].describe()['max']]
    
    df[col] = pd.cut(df[col], edges, labels=labels, duplicates='drop')
    return df
    


# In[18]:


labels = ['not_popular','below_avg','average','popular']

categorize_col(df,'Vote_Average',labels)


# In[19]:


df['Vote_Average'].value_counts()


# In[20]:


df.isnull().sum()


# In[21]:


df.dropna(inplace=True)


# In[22]:


df['Genre'] = df['Genre'].str.split(', ')


# In[27]:


df.head()


# In[28]:


df1 = df.copy


# In[29]:


df = df.explode('Genre').reset_index(drop=True)


# In[30]:


df


# In[32]:


df['Genre'] = df['Genre'].astype('category')


# In[34]:


df['Genre'].dtypes


# In[35]:


df.info()


# In[ ]:





# # Data Visualization

# ### What is the most frequent genre of the movies released on netflix?

# In[38]:


sns.set_style('whitegrid')


# In[40]:


df['Genre'].describe()


# In[42]:


sns.catplot(y='Genre',data=df,kind='count',order=df['Genre'].value_counts().index)
plt.title('Movie Distribution according to Genre')


# ### Which genre has highest vote in "Vote_Average" column?

# In[46]:


sns.catplot(y='Vote_Average',data=df,kind='count',
           order=df['Vote_Average'].value_counts().index)
plt.title('Votes Distribution')


# ### What movie got highest popularity? What's its genre?

# In[47]:


df[df['Popularity'] == df['Popularity'].max()]


# ### What movie got lowest popularity? What's its genre?

# In[48]:


df[df['Popularity'] == df['Popularity'].min()]


# ### Which year has the most movies filmed?

# In[55]:


df[df['Release_Date'] == 2021].value_counts()


# In[60]:


df['Release_Date'].value_counts()


# In[58]:


df['Release_Date'].hist()


# Conclusion
# Q1:What is the most frequent genre of the movies released on netflix?
# ANS: 'Drama' is the most frequent genre in this dataset and has appeared more than 14% among other genres.
# 
# Q2: Which genre has highest vote in "Vote_Average" column?
# ANS: 'Drama' again gets highest popularity among fans.
# 
# Q3: What movie got highest popularity? What's its genre?
# ANS: "Spider Man: No Way Home" has highest popularity rate in this dataset and it has genre of Action, Adventure and Science-Friction.
# 
# Q4: What movie got lowest popularity? What's its genre?
# ANS: "The United States vs. Billie Holiday" and "Threads" has lowest popularity rate in this dataset and it has genre of Music, History, War and Science Friction.
# 
# Q5: Which year has the most movies filmed?
# ANS: Year 2020 has the highest film production rate in this dataset.

# In[ ]:




