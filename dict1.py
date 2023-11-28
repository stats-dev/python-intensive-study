# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin','norway':'oslo' }

# Print europe
print(europe)

## 이번에는 딕셔너리에 값을 추가하는 방법입니다.
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe) # True 가 나타납니다.

# Add poland to europe
europe['poland']='warsaw'

# Print europe
print(europe)


## 수정과 삭제도 같은 원리입니다.
# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia(삭제)
del europe['australia']

# Print europe
print(europe)
