import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data= pd.read_csv("Video_Games.csv")

best_games = [] 

# This code loop through the data frame and makes a new list where every game
# that has a score higher than 80 is selected and the rest is filtered out.
for i in range(len(data)):
    score = data["Critic_Score"][i]   
    if score > 80:                    
        best_games.append(data["Name"][i])
best_games= np.array(best_games)        
print(best_games)
        
