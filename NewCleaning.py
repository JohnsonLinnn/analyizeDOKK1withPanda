#import numpy as np     #library for mathematical functions and mulit-dimensional arrays
import pandas as pd    #library for data manipulation and analysis
#import seaborn as sns  #library for statistical data visualization
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
#import re #this might be regular expression or might be something else
from datetime import datetime    #library to work with time data

#loading the CSV file and check what is inside
df = pd.read_csv("Data.csv") 

df.info()
print("the above is init")
#df.head(5)

#Cleaning the data, and put time information into "date" and "hours"
df[["date","hours"]]=df["time"].str.split("T",expand=True)
df['date_timedata']=df['date']
df['date'] = df['date'].str.replace('-','').astype('int')
df['hours'] = df['hours'].str.replace(':','').astype('int')

#sorting the value with date
df=df.sort_values(by=['date'], ascending=True)


#writing the value into another CSV
df.to_csv('CleanedDataInNoteBook.csv')
df.info()
print(df.head(5))
print("above is what write in csv")
df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")


df=df.groupby(['date']).sum().reset_index()

showdf=df[['date','in','out']]
print(showdf)
showdf.plot.line(x="date", y=["in", "out"])
#plt.show()