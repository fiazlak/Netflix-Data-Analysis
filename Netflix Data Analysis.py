#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install textblob --user


# In[2]:


import numpy as np # linear algebra operations
import pandas as pd # used for data preparation
import plotly.express as px #used for data visualization
from textblob import TextBlob #used for sentiment analysis


# In[3]:


df = pd.read_csv('netflix_titles.csv')


# In[4]:


##Checking number of rows and columns in data


# In[5]:


df.shape


# In[6]:


##Checking content available in Dataset


# In[7]:


df.head()


# In[8]:


##How to check columns name of dataset


# In[9]:


df.columns


# In[10]:


##Taking the count of ratings available


# In[11]:


x = df.groupby(['rating']).size().reset_index(name='counts')
print(x)


# In[12]:


##Creating the Piechart based on Content rating


# In[13]:


pieChart = px.pie(x, values='counts', names='rating', title='Distribution of content ratings on Netflix')
pieChart.show()


# In[14]:


## Analyzing the top 5 Directors on Netflix


# In[15]:


df['director']=df['director'].fillna('Director not specified')
df.head()


# In[16]:


directors_list = pd.DataFrame()
print(directors_list)


# In[17]:


directors_list = df['director'].str.split(',', expand=True).stack()
print(directors_list)


# In[18]:


directors_list = directors_list.to_frame()
print(directors_list)


# In[19]:


directors_list.columns = ['Director']
print(directors_list)


# In[20]:


directors = directors_list.groupby(['Director']).size().reset_index(name='Total Count')
print(directors)


# In[21]:


directors = directors[directors.Director != 'Director not specified']


# In[22]:


print(directors)


# In[23]:


directors = directors.sort_values(by=['Total Count'], ascending = False)
print(directors)


# In[24]:


top5Directors = directors.head()
print(top5Directors)


# In[25]:


top5Directors = top5Directors.sort_values(by=['Total Count'])
barChart = px.bar(top5Directors, x='Total Count', y = 'Director', title = 'Top 5 Directors on Netflix')
barChart.show()


# In[26]:


##Analyzing the top 5 Actors on Netflix


# In[27]:


df['cast']=df['cast'].fillna('No cast specified')
cast_df = pd.DataFrame()
cast_df = df['cast'].str.split(',',expand=True).stack()
cast_df = cast_df.to_frame()
cast_df.columns = ['Actor']
actors = cast_df.groupby(['Actor']).size().reset_index(name = 'Total Count')
actors = actors[actors.Actor != 'No cast specified']
actors = actors.sort_values(by=['Total Count'], ascending=False)
top5Actors = actors.head()
top5Actors = top5Actors.sort_values(by=['Total Count'])
barChart2 = px.bar(top5Actors, x='Total Count', y='Actor', title='Top 5 Actors on Netflix')
barChart2.show()
     


# In[28]:


##Analyzing the content produced on netflix based on years


# In[29]:


df1 = df[['type', 'release_year']]
df1 = df1.rename(columns = {"release_year":"Release Year", "type": "Type"})
df2 = df1.groupby(['Release Year', 'Type']).size().reset_index(name='Total Count')
     


# In[30]:


print(df2)


# In[31]:


df2 = df2[df2['Release Year']>=2000]
graph = px.line(df2, x = "Release Year", y="Total Count", color = "Type", title = "Trend of Content Produced on Netfilx Every Year")
graph.show()


# In[32]:


##Sentiment Analysis of Netflix Content


# In[33]:


df3 = df[['release_year', 'description']]
df3 = df3.rename(columns = {'release_year':'Release Year', 'description':'Description'})
for index, row in df3.iterrows():
  d=row['Description']
  testimonial = TextBlob(d)
  p = testimonial.sentiment.polarity
  if p==0:
    sent = 'Neutral'
  elif p>0:
    sent = 'Positive'
  else:
    sent = 'Negative'
  df3.loc[[index, 2], 'Sentiment']=sent

df3 = df3.groupby(['Release Year', 'Sentiment']).size().reset_index(name = 'Total Count')

df3 = df3[df3['Release Year']>2005]
barGraph = px.bar(df3, x="Release Year", y="Total Count", color = "Sentiment", title = "Sentiment Analysis of Content on Netflix")
barGraph.show()


# In[ ]:





# In[ ]:




