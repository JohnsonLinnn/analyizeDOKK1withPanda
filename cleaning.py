import numpy as np     #library for mathematical functions and mulit-dimensional arrays
import pandas as pd    #library for data manipulation and analysis
import seaborn as sns  #library for statistical data visualization
import matplotlib.pyplot as plt #plotting library
import re #this might be regular expression or might be something else
from datetime import datetime    #library to work with time data
#%matplotlib inline

df = pd.read_csv("Data.csv") 

#df['time'].str.split(r'\d',"T",  expand=True)

print("this is the split")
df[["date","hours"]]=df['time'].str.split("T",expand=True)
#df.info()
print(df)
print("this spliting")
#df["date"]=df['date'].str.replace('-', '')
df['date'] = df['date'].str.replace('-','').astype('int')
df.info()
#print("this is the original sort")

df=df.sort_values(by=['date'], ascending=True)
#df.sort_values(by=['date'], ascending=True)

year1=0
year2=0
year3=0
year4=0

print(df)
for index,row in df.iterrows():
    if row['date']==20150706:
        year1+=row["in"]
    elif row['date']==20150707:
        year2+=row["in"]
    elif row['date']==20150708:
        year3+=row["in"]
#df.to_csv('CleanedData.csv')
print("year1")
print(year1)
print("year2" )
print(year2)
print("year3" )
print(year3)





