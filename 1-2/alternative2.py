n = int(input('출력 갯수 : '))

for _ in range(n//2):
    print('+-', end= '')        # +-를 n//2 개의 출력
    
if n % 2:
    print('+', end= '')         # n이 홀수일 때만 +를 출력
    
print()