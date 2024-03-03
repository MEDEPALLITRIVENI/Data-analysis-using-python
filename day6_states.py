# -*- coding: utf-8 -*-
"""DAY6_States.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14SuD06RfXzfZxrYhORsktxic522bh7gP
"""

import pandas as pd
import seaborn as sns

import seaborn as sns
df=pd.read_csv("/content/data.csv.zip",encoding='latin-1')
df

state='Maharashtra'
location='Pune'
p1=sns.relplot(x='location',y='no2',data=df)

import seaborn as sns
data=df[df['state'] == 'Maharashtra']
sns.barplot(data=data,y='no2',x='location',hue='location')