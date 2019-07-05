#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np 
import pandas as pd 
import os
import matplotlib.pyplot as pl
import seaborn as sns
dir_path = os.path.dirname(os.path.realpath('__file__'))
print(dir_path)
data = pd.read_csv(dir_path + '\\insurance.csv')
data.iloc[:10]


# In[36]:


data.isnull().sum() 
#check if there is a missing data


# In[40]:


from sklearn.preprocessing import LabelEncoder
#sex
label = LabelEncoder()
label.fit(data.sex.drop_duplicates()) 
data.sex = label.transform(data.sex)
data.sex.iloc[:10]


# In[43]:


from sklearn.preprocessing import LabelEncoder
#region
label2=LabelEncoder()
label2.fit(data.region.drop_duplicates())
data.region=label2.transform(data.region)
data.region.iloc[:10]


# In[45]:


#region
le.fit(data.region.drop_duplicates()) 
data.region = le.transform(data.region)
data.region


# In[69]:


x_features = data.drop(["expenses"], axis = 1)
x_features


# In[70]:


y_label=data.expenses
y_label.head(5)


# In[89]:


from sklearn.cross_validation import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.ensemble import RandomForestRegressor
x_train, x_test, y_train, y_test = train_test_split(x_features, y_label, test_size = 0.3 ,random_state = 0)
x_train, x_test, y_train, y_test =x_train.values , x_test.values, y_train.values, y_test.values
x_train


# In[90]:


regression = LinearRegression()
regression.fit(x_train , y_train)

