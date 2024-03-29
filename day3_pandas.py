# -*- coding: utf-8 -*-
"""Day3_pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tkhlOyAlcJnYq-bUSdZlmEFux8cjBQDJ
"""

#importing pandas
import pandas as pd

#pd.series(column,index)
 import pandas as pd
 a=['Triveni','Mahi','Mounie','Varsha','sri','Resh']
 r=pd.Series(a,index=[1,2,3,4,5,6])
 print(r)

a=['Triveni','Mahi','Mounie','Varsha','sri','Resh']
index=[1,2,3,4,5,6]
r=pd.Series(a,index)
print(r)

#loading csv file
dia=pd.read_csv("/content/diabetcsv.csv")
dia

#loading text file
grade=pd.read_csv("/content/demodt.txt",sep=",")
grade

#loading excel
diaxl=pd.read_excel("/content/diabetes.xlsx")
diaxl

#loading excel
diaxl=pd.read_excel("/content/diabetes.xlsx",sheet_name=(1))
diaxl

#loading excel
diaxl=pd.read_excel("/content/diabetes.xlsx",sheet_name="dora")
diaxl

#describing dataframe
grade.describe()

#shape
grade=pd.read_csv("/content/demodt.txt",sep=",")
print(grade.shape)  #get the number of rows and columns
print(grade.shape[0]) #get the number of rows
print(grade.shape[1]) #get the number of columns

df=pd.read_csv("/content/grades_withnulls.csv")
df.dropna(inplace=True)
df

df2=pd.read_csv("/content/grades_withnulls.csv")
mdf=df.dropna()
mdf

df1=pd.read_csv("/content/grades_withnulls.csv")
df1.dropna(inplace=True)
df1

print(df.isnull())

print(df.isnull().sum())

df.dropna()

df

df2=pd.read_csv("/content/grades_withnulls.csv")
mdf=df.dropna()
mdf

df2=pd.read_csv("/content/grades_withnulls.csv")
df2.fillna(555)

df2=pd.read_csv("/content/grades_withnulls.csv")
df2.fillna(555,inplace=True) #changes are saved
df2

#replacing null value with mean values
mydf=pd.read_csv("/content/grades_withnulls.csv")
mv=mydf['SEM1'].mean()
print(mv)
mydf.fillna(mv,inplace=True)
mydf

#access the data
#iloc = integer location , index
#loc = filed names, index
#dfname=loc[index]  --->rows
#df.name.loc[st:stop]  -->>>  range of rows
#df.name.iloc[r_ind,col_index] ---->>rows and columns
mydf.loc[0] #first record , it gives rows

mydf.loc[5] #first five records

mydf.loc[5:7,'SEM1']  #first record

mydf.iloc[10:12,0:2]

mydf[mydf.Grade=='A']

#Print the records who score 9.3 in sem3
#problem statement
mydf[mydf.SEM3==9.3]

mydf.loc[mydf['SEM1'] > 9.8,['Names']]

#access the grades of students who scored more than 9.3 in sem3
mydf.loc[mydf['SEM3'] > 9.7,['Grade']]
#accessing the records with sem3>9.7 but printing only grade column

#accessing using index functiion
print(mydf[mydf.index==7])
print("accessing specific row and column : ")
print(mydf.loc[mydf.index==7,'Grade'])

mydf.drop_duplicates(inplace=True)
print(mydf)

mydf.head() #first 5

mydf.tail() #last 5

#columns1
colnames=mydf.columns #view column nmaes!
print(colnames)

collist=list(mydf.columns)  #view column nmaes!
print(collist)

#rename a column
mydf.rename(columns={'Grade':'GPA'},inplace=True)
mydf.columns

#creating a new column !
#dfname['new col']=values
mydf['conduct']='Good'
mydf

#problem statement
#$create new column average with the values of average marks of sem1,sem2,sem3

mydf['average']=(mydf["SEM1"]+mydf["SEM2"]+mydf['SEM3'])/3
mydf

"""DATA VISUALIZATION WITH PANDAS"""

#plotting with pandas
import pandas as pd
mydf['SEM1'].plot.line()  #dfname=['col'].plot.line()

mydf[['SEM1','SEM2']].plot.line()   #plotting multiple columns

mydf[['SEM1','SEM2']].plot.line(subplots=True)  #two prints seperately

mydf.plot.line(subplots=True)   #to print all columns

mydf.plot(kind='hist',x='Names',y='average')  #y should be numeric
#kind='scatter' (dots)

mydf.to_csv("mydf.csv")   #dfname.to_csv("filename")