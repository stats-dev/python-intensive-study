# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)


# Print cars
print(cars)

#          country  drives_right  cars_per_cap
# 0  United States          True           809
# 1      Australia         False           731
# 2          Japan         False           588
# 3          India         False            18
# 4         Russia          True           200
# 5        Morocco          True            70
# 6          Egypt          True            45

# 이번에는 인덱스를 country로 해볼까?
cars = pd.DataFrame(my_dict, index=my_dict['country'])
print(my_dict['drives_right'])