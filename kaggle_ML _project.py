#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import os
import matplotlib.pyplot as pl
import seaborn as sns
dir_path = os.path.dirname(os.path.realpath('__file__'))
print(dir_path)
data = pd.read_csv(dir_path + '\\insurance.csv')
data.iloc[:10]


# In[2]:


data.isnull().sum() 
#check if there is a missing data


# In[3]:


from sklearn.preprocessing import LabelEncoder
#sex
label = LabelEncoder()
label.fit(data.sex.drop_duplicates()) 
data.sex = label.transform(data.sex)
data.sex.iloc[:10]


# In[4]:


from sklearn.preprocessing import LabelEncoder
#region
label2=LabelEncoder()
label2.fit(data.region.drop_duplicates())
data.region=label2.transform(data.region)
data.region.iloc[:10]


# In[17]:


from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()
label.fit(data.smoker.drop_duplicates()) 
data.smoker = label.transform(data.smoker)
data.smoker.iloc[:10]


# In[18]:


x_features = data.drop(["expenses"], axis = 1)
x_features.head(5)


# In[20]:


y_label=data.expenses
y_label.head(5)


# In[21]:


x_train, x_test, y_train, y_test = train_test_split(x_features, y_label, test_size = 0.3 ,random_state = 0)
x_train, x_test, y_train, y_test =x_train.values , x_test.values, y_train.values, y_test.values
x_train


# In[22]:


regression = LinearRegression()
regression.fit(x_train , y_train)


# In[26]:


y_train_pred = regression.predict(x_train)
y_test_pred = regression.predict(x_test)

print(regression.score(x_test,y_test))

