# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('./cars.csv')

# Print out cars
print(cars)
#   Unnamed: 0  cars_per_cap        country  drives_right
# 0         US           809  United States          True
# 1        AUS           731      Australia         False
# 2        JPN           588          Japan         False
# 3         IN            18          India         False
# 4         RU           200         Russia          True
# 5        MOR            70        Morocco          True
# 6         EG            45          Egypt          True

## 저걸 지워버리자.. index_col=0
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)