import copy

x = [[1,2,3], [4,5,6]]

y = x.copy()

print(f'얕은 카피 : {y}')

x[0][1] = 9

print(x)
print(y)

print('-------------------------------------------')

deep_y = copy.deepcopy(x)

x[0][1] = 0

print(x)

print(f'Deep Copy of x : {deep_y}')