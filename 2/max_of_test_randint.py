# 배열 원소의 최댓값을 구해서 출력하기

import random
from max import max_of

num = int(input('난수의 갯수 : '))
lo = int(input('난수의 최솟값 : '))
hi = int(input('난수의 최댓값 :'))
x = [None] * num

for i in range(num):
    x[i] = random.randint(lo, hi)
    
print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)} 입니다.')