# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('./cars.csv')

# Print out cars
print(cars)

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)