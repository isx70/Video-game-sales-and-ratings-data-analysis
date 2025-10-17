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


