# a 부터 b 까지 정수의 합 구하기 (for문)

print('a 부터 b 까지 정수의 합')
a = int(input('a = '))
b = int(input('b = '))

if a > b:
    a,b = b, a  # a와 b를 오름차순으로 정렬
    
sum = 0
for i in range(a, b+1):
    sum += i

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')