#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Loading the require libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[9]:


#Loading the IPL 2022 Dataset
df1 = pd.read_csv(r"C:\Users\vimal\OneDrive\Desktop\Dataset\IPL 2022\IPL_Matches_2022.csv")


# In[10]:


df1


# In[11]:


#Having a Glance at first 5 records of datasets
df1.head()


# In[13]:


#Looking at No. of Rows ans Columns in the dataset
df1.shape


# In[15]:


#Getting the frequency of most player of the match awards
df1['Player_of_Match'].value_counts()


# In[83]:


#Getting the Top 5 most player of the match awards
df1['Player_of_Match'].value_counts()[0:5]


# In[82]:


list(df1['Player_of_Match'].value_counts()[0:5].keys())


# In[23]:


#Making Bar plot bar Top 5 Players of the match awards
plt.figure(figsize=(10,5))
plt.title('Most Player of the Match')
plt.bar(list(df1['Player_of_Match'].value_counts()[0:5].keys()),df1['Player_of_Match'].value_counts()[0:5], color= ["Orange"])
plt.show


# In[55]:


#Find out the Most matches winning Team
df1['WinningTeam'].value_counts()


# In[56]:


#Find out the Top 5 Most matches winning Team
df1['WinningTeam'].value_counts()[0:5]


# In[62]:


list(df1['WinningTeam'].value_counts()[0:5].keys())


# In[24]:


#Making Bar plot bar Top 5 Most matches winning team
plt.figure(figsize=(13,5))
plt.title('Most Winning team')
plt.bar(list(df1['WinningTeam'].value_counts()[0:5].keys()),df1['WinningTeam'].value_counts()[0:5], color=["Green"])
plt.show


# In[14]:


#Find out the Most tosses winning Team
df1['TossWinner'].value_counts()


# In[77]:


#Extracting the data where a team won batting first
Battingfirst = df1[df1['WonBy']=='Runs']


# In[16]:


#Looking at the Data
Battingfirst


# In[78]:


#Making a histogram
plt.figure(figsize=(7,7))
plt.title('Distribution of runs')
plt.hist(Battingfirst['Margin'],bins=10)
plt.xlabel('Runs')         
plt.show


# In[30]:


#Find out the no of matches wins after batting first 
Battingfirst['WinningTeam'].value_counts()


# In[138]:


#Find out the Top 3 no of matches wins after batting first 
Battingfirst['WinningTeam'].value_counts()[0:3]


# In[31]:


list(Battingfirst['WinningTeam'].value_counts().keys())


# In[27]:


#Making Bar plot Top 3 no of matches wins after batting first 
plt.figure(figsize=(10,5))
plt.title('Most Winning team in Batting first')
plt.bar(list(Battingfirst['WinningTeam'].value_counts()[0:3].keys()),Battingfirst['WinningTeam'].value_counts()[0:3], color=["Blue","Orange", "Red"
])
plt.show


# In[66]:


#Making Piechart for no. of matches won in Batting first 
plt.figure(figsize=(7,7))
plt.title('Most Winning Percent in Batting first')
plt.pie(Battingfirst['WinningTeam'].value_counts(),labels=list(Battingfirst['WinningTeam'].value_counts().keys()), autopct='%0.1f%%')
plt.show


# In[80]:


#Extracting the data where a team won batting second
Battingsecond = df1[df1['WonBy']=='Wickets']


# In[81]:


#Looking at the data
Battingsecond.head()


# In[82]:


#Making a histogram 
plt.figure(figsize=(7,7))
plt.hist(Battingsecond['Margin'], bins=5, color='Red')
plt.xlabel('Wickets')         
plt.show


# In[83]:


#Find out the no of matches wins after batting second
Battingsecond['WinningTeam'].value_counts()


# In[88]:


#Find out the Top 3 no of matches wins after batting second
Battingsecond['WinningTeam'].value_counts()[0:3]


# In[89]:


list(Battingsecond['WinningTeam'].value_counts()[0:3].keys())


# In[92]:


#Making Bar plot Top 3 no of matches wins after batting first 
plt.figure(figsize=(12,5))
plt.title('Most Winning team in Batting Second')
plt.bar(list(Battingsecond['WinningTeam'].value_counts()[0:3].keys()),Battingsecond['WinningTeam'].value_counts()[0:3],  color=["Blue","Orange", "Red"])
plt.show


# In[87]:


#Making Piechart for no. of matches won in Batting second
plt.figure(figsize=(7,7))
plt.title('Most Winning Percent in Batting Second')
plt.pie(Battingsecond['WinningTeam'].value_counts(),labels=list(Battingsecond['WinningTeam'].value_counts().keys()),autopct='%0.1f%%')
plt.show


# In[97]:


#Finding out How many times a team won the toss and match
import numpy as np
np.sum(df1['TossWinner']==df1['WinningTeam'])


# In[76]:


#Finding out Percent of How many times a team won the tosses and matches
36/74


# In[ ]:




