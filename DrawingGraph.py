import pandas as pd    #library for data manipulation and analysis
import matplotlib.pyplot as plt
from datetime import datetime    #library to work with time data

#loading the CSV file and peek what is inside the Pandora's Box
df = pd.read_csv("CleanedDataInNoteBook.csv") 
df.info()
#df.head(5)

#convert date from string into datatime(a data type in panda) 
df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")
#check if I fuck up or not 
df.info()

df=df.groupby(['date']).sum().reset_index()
#prepare the data for graph
showdf=df[['date','in','out']]
showdf.info()

#do some filter because the data is to many to show in one graph
start_date = "2019-1-1"
end_date = "2019-12-31"
#print(showdf)
after_start_date = showdf["date"] >= start_date
before_end_date = showdf["date"] <= end_date
between_two_dates = after_start_date & before_end_date
showdf = df.loc[between_two_dates]

#print(showdf)

#plz work, just show me the graph
fig=showdf.plot.line(x="date", y=["in", "out"],figsize=(10,5))
plt.savefig('19chart.png')
plt.show()
