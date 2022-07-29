# Import pandas library
import pandas as pd

# Load csv and chunk it
rows = pd.read_csv("./resources/data/train.csv", chunksize=1666673) 
for i, chuck in enumerate(rows): 
    chuck.to_csv(f'./resources/data/ratings_{i}.csv') # i is for chunk number of each iteration 