n = int(input('몇 개를 출력 : '))
w = int(input('줄 바꿈 :'))

for i in range(n):
    print('*', end= '')
    if i % w == w - 1:          # n번 판단
        print()                 # 줄바꿈
        
if n % w:                       # 1번 판단
    print()                     # 줄바꿈
    
    
    