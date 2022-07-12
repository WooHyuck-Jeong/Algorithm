# 쉐이커 정렬

from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    """쉐이커 정력"""
    left= 0
    right= len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):        # 뒤에서 앞으로 스캔
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        left = last
        
        for j in range(left, right):            # 앞에서 뒤로 스캔
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                last = j
            right = last
    
    # ccnt = 0  # 비교 횟수
    # scnt = 0  # 교환 횟수
    # left = 0
    # n = len(a)
    # right = len(a) - 1
    # last = right
    # i = 0
    # while left < right:
    #     print(f'패스{i + 1}')
    #     i += 1
    #     for j in range(right, left, -1):
    #         for m in range(0, n - 1):
    #            print(f'{a[m]:2}' + ('  ' if m != j - 1 else
    #                                 ' +' if a[j - 1] > a[j] else ' -'),
    #                  end='')
    #         print(f'{a[n - 1]:2}')
    #         ccnt += 1
    #         if a[j - 1] > a[j]:
    #             scnt += 1
    #             a[j - 1], a[j] = a[j], a[j - 1]
    #             last = j
    #     left = last
    #     for m in range(0, n - 1):
    #        print(f'{a[m]:2}', end='  ')
    #     print(f'{a[n - 1]:2}')

    #     if (left == right):
    #          break
    #     print(f'패스 {i + 1}')
    #     i += 1
    #     for j in range(left, right):
    #         for m in range(0, n - 1):
    #            print(f'{a[m]:2}' + ('  ' if m != j else
    #                                 ' +' if a[j] > a[j + 1] else ' -'),
    #                  end='')
    #         print(f'{a[n - 1]:2}')
    #         ccnt += 1
    #         if a[j] > a[j + 1]:
    #             scnt += 1
    #             a[j], a[j + 1] = a[j + 1], a[j]
    #             last = j
    #     right = last
    #     for m in range(0, n - 1):
    #        print(f'{a[m]:2}', end='  ')
    #     print(f'{a[n - 1]:2}')
    # print(f'비교를 {ccnt}번 했습니다.')
    # print(f'교환을 {scnt}번 했습니다.')
            
if __name__ == '__main__':
    num = int(input('원소 수 : '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))
        
    shaker_sort(x)
    
    print('정렬')
    
    for i in range(num):
        print(f'x[{i}] = {x[i]}')