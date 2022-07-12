# 버블 정렬 과정 구현

from typing import MutableSequence

def bubble_sort(a : MutableSequence) -> None:
    """버블 정렬"""
    ccnt = 0        # 비교 횟수
    scnt = 0        # 교환 횟수
    n = len(a)
    for i in range(n-1):
        print(f'패스 {i + 1}')
        for j in range(n-1, i, -1):
            for m in range(0, n-1):
                print(f'{a[m] : 2}' + ('  ' if m != j-1 
                                       else ' +'            # 교환할 경우
                                       if a[j-1] > a[j] 
                                       else ' -'), end='')  # 교환하지 않을 경우
            
            print(f'{a[n-1]:2}')
            ccnt += 1
            if a[j-1] > a[j]:
                scnt += 1
                a[j-1], a[j] = a[j], a[j-1]
        for m in range(0, n-1):
            print(f'{a[m]:2}', end= '  ')
        print(f'{a[n-1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')
    
if __name__ == '__main__':
    print('버블 정렬 수행')
    num = int(input('원소 수 : '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))
        
    bubble_sort(x)
    
    print('오름차순 정렬')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')