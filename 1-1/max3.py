# 세 정수를 입력받아 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a :'))
b = int(input('정수 b :'))
c = int(input('정수 c :'))

maximum = a                     # maximum에 a값을 대입

if b > maximum : maximum = b    # b의 값이 maximum보다 크면, maximum에 b의 값을 대입
if c > maximum : maximum = c    # c의 값이 maximum보다 크면, maximum에 c의 값을 대입

print(f'최댓값은 {maximum} 입니다.')
