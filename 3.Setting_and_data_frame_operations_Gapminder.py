# Pandas selection
from gapminder import gapminder as gp
import pandas as pd
import numpy as np

# view the head of the data
df = gp.copy()
print(df.head(10)) 
df_orig = df.copy()


# ------------------------------------ Setting  --------------------------------------------------#

df.iat[0, 2] = '2020' # Set values by position
print(df.iat[0,2])

df.loc[:, 'pop'] = np.array([5] * len(df)) #Setting by assignment with a NumPy array
print(df)
print(np.array(5)*len(df))


# # ------------------------------------ Missing data  --------------------------------------------------#
df[1:1000] = np.nan
print(df)


# #Drop any rows that have missing data
df2= df.copy()
print(df2.dropna(how='any'))
# # Filling missing data
print(df[2:5].fillna(value =5))
# # Search for values using a boolean mask where equal to NA#
print(pd.isna(df))
print(any(pd.isna(df))) # Check to see if the missing values are contained anywhere in df


# # ------------------------------------ Operations on frames-------------------------------------------------#
# #########################################Stats###############################################################

df = df_orig.copy()
print(df.mean())
print(df.mean(1))



# #########################################Applying functions to the data#######################################
df_sub = df.loc[:,['pop']]
df_sub_copy = df_sub
print(df_sub.apply(np.cumsum))

#Lambda functions
print(df_sub_copy.apply(lambda x: x.max() - x.min()))
# #########################################Histogramming########################################################
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())
