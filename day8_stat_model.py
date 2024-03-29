# -*- coding: utf-8 -*-
"""DAY8_Stat_Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YQRyVjuEgEJ_U38hz32cl3yJO-fuBpjn
"""

#Hypothesis testing :
import numpy as np
from scipy import stats

#Generate two sets of sample data

data1=np.array([28,21,26,29,23])
data2=np.array([21,27,25,28,19])
print(data1.mean())
print(data1.mean())

#perform t-test assumig unequal variances
t_stat,p_value=stats.ttest_ind(data1,data2,equal_var=False)

#Print the results
print(("t-statistic:",t_stat))
print("P-value",p_value)

#set significant level
alpha =0.05

if p_value < alpha:
  print("Reject the null hypothesis.the means are significant")
else:
  print("Fail to reject the null hypothesis.the means are  not significant")

"""Request Analysis"""

import pandas as pd
df=pd.read_csv('/content/Vaccine.csv')

df

group_A=df['Efficiency']
group_B=df['Rec_Rate']
t_stat,p_value=stats.ttest_ind(group_A,group_B)
print("t-Val",t_stat)
print("P-val",p_value)

alpha=0.05



if p_value < alpha:
  print("H0-related not different")
else:
  print("H1-not related significantly different")

"""ANOVA TESTING"""

dfA=df[df['Vaccine']=='A']['Efficiency']
dfB=df[df['Vaccine']=='B']['Efficiency']

dfA

f_stat,p_value=stats.f_oneway(dfA,dfB)
print("F-statistic:",f_stat)
print("p-value:",p_value)

"""INTERPOLATION"""

from scipy import interpolate
#Interpolation
x_data=np.array([0,1,2,3,4])
y_data=np.array([0,2,1,3,5])
interp_func=interpolate.interp1d(x_data,y_data,kind='linear')
interp_result=interp_func(2.5)
print("Interpolation REsult : ",interp_result)