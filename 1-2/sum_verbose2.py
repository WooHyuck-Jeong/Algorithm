# a 부터 b 까지 정수의 합 구하기

a = int(input('a = '))
b = int(input('b = '))

if a > b:
    a,b = b,a
    
sum = 0

for i in range(a,b):
    print(f'{i}+', end= '')
    sum += i
    
print(f'{b} =', end= '')
sum += b

print(sum)