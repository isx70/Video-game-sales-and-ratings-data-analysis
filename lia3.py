import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


#Part 2 : Preliminary steps
data= pd.read_csv("Video_Games.csv")

#! overview of data
#print(data.head())

#print(data.shape)

#print(data.info())

#print(data.describe())

#2 identify and drop duplicates

#print(data.duplicated().sum())
#there are 0 duplicates already so we dont need to do another line of code

#3 Identify and manage missing values:
    
#print(data.isnull().sum())

#4 Correct data types and formats:

#data["User_Score"]=pd.to_numeric(data["User_Score"],errors="coerce")
#print (data.info())

#Part 3 : Univariate non-graphical EDA


numeric = data.select_dtypes(include='number').columns
rows = []

for col in numeric:
    s = data[col]
    rows.append([
        col,
        s.mean(),
        s.median(),
        s.mode().iloc[0],
        s.std(),
        s.var(),
        s.skew(),
        s.kurt(),
        s.quantile(0.25),
        s.quantile(0.50),
        s.quantile(0.75)
    ])

summary = pd.DataFrame(rows, columns=[
    "variable","mean","median","mode","std","var",
    "skew","kurt","q25","q50","q75"
])

print(summary)

#Part 4: Univariate graphical EDA

#sns.displot(data=data,x="NA_Sales", kind="kde")
#sns.displot(data=data,x=col, hue="NA_Sales")