# 1부터 n까지 정수의 합 구하기(for문)

print('1 부터 n 까지 정수의 합 구하기')

n = int(input('정수 n을 입력 : '))

sum = 0
for i in range(1, n+1):
    sum += i    # sum에 i를 더함
    
print(f'1 부터 {n}까지 정수의 합은 {sum} 입니다.')