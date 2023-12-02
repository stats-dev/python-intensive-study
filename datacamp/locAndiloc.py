# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JAP']) #Series
# print(cars.loc[['JAP']]) #dataframe
print(cars.iloc[2])

# Print out observations for Australia and Egypt
# print(cars.loc[['AUS','EG']])
print(cars.iloc[[1,6]])


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU','MOR'], ['country','drives_right']])

#             country  drives_right
# country_ab                       
# RU           Russia          True
# MOR         Morocco          True


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right']) #Series only one []

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']]) #Sub-DataFrame

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
