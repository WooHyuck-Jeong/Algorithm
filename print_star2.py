n = int(input('몇 개를 출력 :'))
w = int(input('줄 바꿈 : '))

for _ in range(n//w):
    print('*' * w)
    
rest = n % w
if rest:
    print('*' * rest)