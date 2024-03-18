import pandas as pd
import numpy as np
import webbrowser


file_path = '/Users/simonnordlund/Downloads/watchlist-simonnor-2024-03-03-23-33-utc.csv' # Loads the CSV file
df = pd.read_csv(file_path) #Reads the CSV file.


column_lists = {col: df[col].tolist() for col in df.columns} # Converts each column to a list 

links = column_lists['Letterboxd URI']
names = column_lists['Name'] #Access the value of the key "Name" and store it as names .

for i in range(4):
    movie = round(np.random.uniform(0,len(names))) #Creates a uniformly random integer that corresponds to a movie in my watchlist.
    #print(names[movie] + " This is the link " + links[movie])
    webbrowser.open(links[movie])



