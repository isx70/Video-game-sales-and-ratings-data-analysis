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

print(data.duplicated().sum())
#there are 0 duplicates already so we dont need to do another line of code

#3 Identify and manage missing values:

data["User_Score"]=pd.to_numeric(data["User_Score"],errors="coerce")
data['Name'] = data['Name'].fillna("Unknown")
data['Genre'] = data['Genre'].fillna(data['Genre'].mode()[0])
data['Publisher'] = data['Publisher'].fillna(data['Publisher'].mode()[0])
data['Year_of_Release'] = data['Year_of_Release'].fillna(data['Year_of_Release'].mode()[0])   
#data = data.dropna(subset=['User_Score','User_Count',"Critic_Score","Critic_Count","Developer","Rating"])


#print(data.isnull().sum())

#4 Correct data types and formats:

data["User_Score"]=pd.to_numeric(data["User_Score"],errors="coerce")
#print (data.info())

#Part 3 : Univariate non-graphical EDA

numeric = data.select_dtypes(include='number').columns
num_rows = []

for col in numeric:
    c = data[col]
    num_rows.append([col,c.mean(),c.median(),c.mode().iloc[0],c.std(),c.var(),
    c.skew(),c.kurt(),c.quantile(0.25),c.quantile(0.50),c.quantile(0.75)])

summary_num = pd.DataFrame(num_rows, columns=["variable","mean","median","mode",
"std","var","skew","kurt","q25","q50","q75"])

#print(summary_num)


categorical = data.select_dtypes(include='object').columns
cat_rows = []

for col in categorical:
    s = data[col]
    cat_rows.append([col,s.value_counts(),s.value_counts(normalize=True),s.mode().iloc[0],                
    s.nunique()])

summary_cat = pd.DataFrame(cat_rows, columns=["variable","frequency_counts","proportions",
"mode","unique_categories"])

#print(summary_cat)




#Part 4 Univariate graphical EDA


# Plot 1 – NA_Sales ECDF (log scale)
sns.displot(data=data, x='NA_Sales', kind='ecdf')
plt.xscale('log')
plt.title("ECDF of NA Sales (log scale)")
plt.show()

# Plot 2 – EU_Sales KDE (log scale)
sns.displot(data=data, x='EU_Sales', kind='kde')
plt.xscale('log')
plt.title("KDE of EU Sales (log scale)")
plt.show()

# Plot 3 – JP_Sales ECDF (log scale)
sns.displot(data=data, x='JP_Sales', kind='ecdf')
plt.xscale('log')
plt.title("ECDF of JP Sales (log scale)")
plt.show()

# Plot 4 – Other_Sales KDE (log scale)
sns.displot(data=data, x='Other_Sales', kind='kde')
plt.xscale('log')
plt.title("KDE of Other Sales (log scale)")
plt.show()

# Plot 5 – Global_Sales ECDF (log scale)
sns.displot(data=data, x='Global_Sales', kind='ecdf')
plt.xscale('log')
plt.title("ECDF of Global Sales (log scale)")
plt.show()

# Plot 6 – User_Count ECDF (log scale)
sns.displot(data=data, x='User_Count', kind='ecdf')
plt.xscale('log')
plt.title("ECDF of User Count (log scale)")
plt.show()

# Plot 7 – Year_of_Release (custom bins)
sns.displot(data=data, x='Year_of_Release', bins=int(len(data)**0.5), kind='hist')
plt.title("Year of Release  Histogram ")
plt.show()

# Plot 8 – Critic_Score (conditioning + density)
sns.displot(data=data, x='Critic_Score', hue='Genre', kind='hist', stat='density', bins=25)
plt.title("Critic Score Density Histogram by Genre")
plt.show()

# Plot 9 – User_Score (dodge bars)
sns.displot(data=data, x='User_Score', hue='Genre', multiple='dodge', kind='hist', bins=20)
plt.title("User Score Dodge Histogram by Genre")
plt.show()

# Plot 10 – Critic_Count (stacked histogram)
sns.displot(data=data, x='Critic_Count', hue='Genre', multiple='stack', kind='hist', bins=30)
plt.title("Critic Count Histogram by Genre")
plt.show()


#Part 5 Multivariate non-graphical EDA

#Crostab 1

tab1 = pd.crosstab(data['Genre'], data['Rating'], normalize='index')
print(tab1)


#Crosstab 2 
tab2 = pd.crosstab(data['Platform'], data['Genre'], normalize='columns')
print(tab2)   


#Crosstab 3
tab3 = pd.crosstab(data['Developer'], data['Rating'], normalize=True)
print(tab3)


#Crosstab 4
tab4 = pd.crosstab([data['Genre'], data['Rating']],data['Platform'],normalize='index')
print(tab4)

#Part 6 Multivariate graphical EDA

#6.1
#a (Q3)
sns.relplot(data=data, x= "Critic_Score", y= "Global_Sales", col= pd.cut(data["Year_of_Release"], bins=[1995, 2000, 2005, 2010, 2016],labels=["1995–1999", "2000–2004", "2005–2009", "2010–2015"]), kind= "scatter").set(yscale="log")
#The graph shows that the critic score and global sales have an important correlation

#b (Q1)
sns.relplot(data=data[(data["Year_of_Release"] >= 2000) & (data["Year_of_Release"] <= 2016)],x="Critic_Score",y="Global_Sales",hue="User_Score",size="Critic_Count",col="Genre",kind="scatter",col_wrap=3).set(yscale="log")

#c (Q3)
sns.relplot(data=data,x="Year_of_Release",y="Critic_Score",kind="line")

#d (Q2)
data["Score_Diff"] = data["Critic_Score"] / 10 - data["User_Score"]
sns.relplot(data=data,x="Year_of_Release",y="Score_Diff",kind="line",errorbar=("sd"))

#e (Q1)
sns.lmplot(data=data[(data["Year_of_Release"] >= 2000) & (data["Year_of_Release"] <= 2016)],x="Critic_Score",y="Global_Sales",line_kws={'color': 'red'}).set(yscale="log")

#_______________________________________________________________________________________________________________________________________
#6.2
#a (Q4)
sns.catplot(data=data[(data["Critic_Score"] >= 80) & (data["Global_Sales"] >= 1)], y="Publisher", x="Critic_Score", kind="strip", jitter=True)

#b (Q2)
sns.catplot(data=data, y="Genre", x="Score_Diff", kind="strip", jitter=False)

#c (Q5)
sns.catplot(data=data[data["Genre"].isin(data["Genre"].value_counts().index[:6])].sample(150), x="Genre", y="NA_Sales", hue="Rating", kind="swarm").set(yscale="log")
#(limited the sample because this code crashed my spyder)

#d (Q5)
sns.catplot(data=data[(data["Genre"].isin(data["Genre"].value_counts().index[:6])) & (data["Rating"].isin(["E", "M"]))],x="Genre", y="EU_Sales", hue="Rating", kind="box",).set(yscale="log")

#e (Q5)
sns.catplot(data=data[(data["Genre"].isin(data["Genre"].value_counts().index[:6])) & (data["Rating"].isin(["E", "M"]))],x="Genre", y="JP_Sales", hue="Rating", kind="boxen",).set(yscale="log")

#f (Q5)
sns.catplot(data=data[(data["Genre"].isin(data["Genre"].value_counts().index[:6])) & (data["Rating"].isin(["E", "M"]))],x="Genre", y="NA_Sales", hue="Rating", kind="violin",split=True).set(yscale="log")
#Here the fatness doesnt show the number but the density, so even if there is more M games in shooter, all E games performed similarly

#g (Q5)
g = sns.catplot(data=data[data["Genre"].isin(data["Genre"].value_counts().index[:6])], x="Genre", y="NA_Sales", kind="violin", inner=None).set(yscale="log")
sns.stripplot(data=data[data["Genre"].isin(data["Genre"].value_counts().index[:6])].sample(1000), x="Genre", y="NA_Sales", color="k", size=2, jitter=True, ax=g.ax)
#sample because the points were not readable here the dots only appear after 10^-2 because of the nature of the data in which a lot of game have near 0 sales, so only high selling games are showed in the dots

#h (Q4)
#sns.catplot(data=data[(data["Critic_Score"] >= 80) & (data["Global_Sales"] >= 1)], y="Publisher", x="Critic_Score", hue="Rating", kind="bar", errorbar=('ci', 97))
sns.catplot(data=data[(data["Critic_Score"] >= 80) & (data["Global_Sales"] >= 1) & (data["Publisher"].isin(data[(data["Critic_Score"] >= 80) & (data["Global_Sales"] >= 1)]["Publisher"].value_counts().index[:3]))], y="Publisher", x="Critic_Score", hue="Rating", kind="bar", errorbar=('ci', 97))

#i (Q5)
sns.catplot(data=pd.melt(data[data["Genre"].isin(data["Genre"].value_counts().index[:6])], id_vars="Genre", value_vars=["NA_Sales", "EU_Sales", "JP_Sales"], var_name="Region", value_name="Sales"), x="Genre", y="Sales", hue="Region", kind="point", errorbar=("ci", 90), linestyles="--")
#A new genre variable was added for this graph to be very precise, even tho var wasn't studied in class.

#j (Q2)
data["Diff_of_1.5"] = ((data["Critic_Score"] / 10 - data["User_Score"]) >= 1.5)
sns.catplot(data=data, x="Diff_of_1.5", kind="count")

