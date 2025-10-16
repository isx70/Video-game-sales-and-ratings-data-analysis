import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("Video_Games.csv")


        
for i in range(len(data)):
    score = data["Critic_Score"][i]   
    if score > 75:                    
        print(data["Name"][i])