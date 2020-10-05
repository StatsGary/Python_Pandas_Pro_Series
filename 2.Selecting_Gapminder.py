# Pandas selection
from gapminder import gapminder as gp
import pandas as pd
import numpy as np

# view the head of the data
df = gp.copy()
print(df.head(10)) 

# Sorting
# #Sort by value
print(df.sort_values(by=['pop', 'year'], ascending=False))

#------------------------SELECTION-------------------------------
# Selection by 1 x column
print(df['pop'])
# Selection by more than 1 column
print(df[['country', 'pop']])
# Slicing rows
print(df[0:10]) #Slicing rows
# Selection by label
print(df.loc[:, ['lifeExp', 'pop']])
# #Selection with both end points
print(df.loc[0:10, ['lifeExp', 'pop']])
# Selection by position
print(df.iloc[300])
#Integer slicing
print(df.iloc[3:5, 0:2]) 
print(df.iloc[[1, 2, 4], [0, 4]]) #Same as slicing by vector use numpy lists
print(df.iloc[1:9, :]) #Slicing rows explicitly
print(df.iloc[:, 1:4]) #Slicing columns explicitly
print(df.iloc[1, 1]) #Getting a value explicitly
print(df.iat[1, 1]) #Fast access to a scalar explicitly

# #Boolean indexing
pop_filter = 30000000
print(df[df['pop'] > pop_filter]) #Using operators to subset