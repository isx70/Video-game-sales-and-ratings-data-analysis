import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data= pd.read_csv("Video_Games.csv")

best_games = [] 
best_games_score=[]
best_games_sales=[]
best_games_na_sales=[]
best_games_eu_sales=[]
best_games_jp_sales=[]
best_games_user_score=[]
top_publishers_names=[]
top_publishers_sales=[]
genre_labels=[]
genre_values=[]
top15 = data.sort_values("Global_Sales", ascending=False).head(15)

# This code loop through the data frame and makes a new list where every game
# that has a score higher than 80 is selected and the rest is filtered out.
for i in range(len(data)):
    score = data["Critic_Score"][i]   
    if score > 80:                    
        best_games.append(data["Name"][i])
        best_games_score.append(data["Critic_Score"][i])
        best_games_sales.append(data["Global_Sales"][i])
        best_games_na_sales.append (data["NA_Sales"][i])
        best_games_eu_sales.append (data["EU_Sales"][i])
        best_games_jp_sales.append (data["EU_Sales"] [i])
        best_games_user_score.append (data["User_Score"])
        top_publishers_names.append (data["Publisher"])
        top_publishers_sales.append (data["Global_Sales"])
        genre_labels.append (data["Genre"])
        genre_values.append (data["Global_Sales"])
        top_15_games = list(top15["Global_Sales"])  
# To show that the filtering loop worked
print(best_games)

# (d) Historigramm grid plot showing distribution of critics scores for all games
plt.title("Distribution of critics scores for all games")
plt.xlabel("Critic scores")
plt.ylabel("Number of games")
plt.hist(data["Critic_Score"])
plt.grid(axis="y")
plt.show()

# (e) Plot containing two subploats representing the distribution of games that were the most sold in NA and EU
#NA
plt.subplot(1, 3, 1)
plt.title("Distribution of NA video game sales")
plt.xlabel("NA vdg sales in million")
plt.ylabel("Number of games")
plt.hist(best_games_na_sales)
#EU
plt.subplot(1, 3, 3)
plt.title("Distribution of EU video game sales")
plt.xlabel("EU vdg sales in million")
plt.ylabel("Number of games")
plt.hist(best_games_eu_sales)
plt.show()

# (f) Scatter plot
#Plot of how each of the best games sold in NA compared on how it saled in Japan
plt.title("Best video games sales in NA vs in Japan")
plt.xlabel("Video game sales in NA")
plt.ylabel("Video game sales in Japan")
plt.scatter (best_games_na_sales,best_games_jp_sales)
plt.show()

#Plot of how the rating scores affect the sales of the best games
plt.title("Relationship between the critic scores and the global sales of the best video games")
plt.xlabel("Critic scores")
plt.ylabel("Video game global sales")
plt.scatter (best_games_score,best_games_sales)
plt.show()

#Multi line plot showing the correlation between critic/user score and global sales

plt.title("Comparison of critic score, user score, and global sales of top 20 video games")
plt.xlabel("Game index")
plt.ylabel("Value (scaled)")
plt.plot(range(len(best_games)), best_games_score, color='r', linestyle='-', label='Critic Score')
plt.plot(range(len(best_games)), np.array(best_games_user_score) * 10,
         color='b', linestyle='--', label='User Score (x10)')
plt.plot(range(len(best_games)), np.array(best_games_sales) * 10,
         color='g', linestyle=':', label='Global Sales (x10)')
plt.legend()
plt.show()


#Bar Plot showing the top 5 pblishers with the most video game sales

plt.title("Top 5 publishers by total global video game sales")
plt.xlabel("Publisher")
plt.ylabel("Global sales (in million units)")
plt.bar(top_publishers_names, top_publishers_sales, color=['blue', 'orange', 'green', 'pink', 'violet'])
plt.show()

#Grid showing the critic/user score and the user count of the 15 most selling games

plt.title("Critic score, user score, and user count for top 15 games")
plt.xlabel("Game index")
plt.ylabel("Value")
plt.plot(top_15_games["Critic_Score"], color='r', label='Critic Score')
plt.plot(top_15_games["User_Score"], color='b', label='User Score')
plt.plot(top_15_games["User_Count"], color='g', label='User Count')
plt.legend()
plt.grid(True)
plt.show()


#Pie Chart showing which genre has the most global sales.

plt.title("Proportion of global sales by genre")
plt.pie(genre_values, labels=genre_labels, autopct='%1.1f%%', startangle=140)
plt.show() 
