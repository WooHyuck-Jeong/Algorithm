from typing import Any, Sequence

def bin_search(a : Sequence, key : Any) -> int :
    pl = 0
    pr = len(a) - 1
    
    print('    |', end= '')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4 * len(a) + 2) * '-')
    
    while True:
        pc = (pl + pr) // 2
        
        print('    |', end= '')
        if pl != pc:
            print((pl * 4 + 1) * ' ' + '<-' + ((pc - pl) * 4) * ' ' + '+', end='')
        else:
            print((pc * 4 + 1) * ' ' + '<+', end='')
        if pc != pr:
            print(((pr - pc) * 4 - 2) * ' '+'->')
        else:
            print('->')
        print(f'{pc:3}|', end='')
        for i in range(len(a)):
            print(f'{a[i]:4}', end= '')
        print('\n |')
        
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr =pc - 1
        if pl > pr:
            break
    return -1
        
if __name__ == '__main__':
    num = int(input('원소 수 : '))
    x = [None] * num
    
    x[0] = int(input('x[0] : '))
    
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= x[i-1]:
                break
    
    ky = int(input('검색 값 : '))
    
    idx = bin_search(x, ky)
    
    if idx == -1:
        print('검색값 존재 X')
    else:
        print(f'검색 값은 x[{idx}]에 존재')