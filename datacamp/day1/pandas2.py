# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country']) # Pandas Series


# Print out country column as Pandas DataFrame
print(cars[['country']]) # Pandas DataFrame

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])


## slicing in pandas
# Print out first 3 observations
print(cars[0:3]) # slicing in pandas

# Print out fourth, fifth and sixth observation
print(cars[3:6])
#             cars_per_cap  country  drives_right
# country_ab                                     
# IN                    18    India         False
# RU                   200   Russia          True
# MOR                   70  Morocco          True
