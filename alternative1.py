# +, - 번갈아가면서 출력

n = int(input('출력 갯수 : '))

for i in range(n):
    if i % 2:                   # 홀수인 경우 - 출력
        print('-', end='')
        
    else:                       # 짝수인 경우 + 출력
        print('+', end= '')
        
print()