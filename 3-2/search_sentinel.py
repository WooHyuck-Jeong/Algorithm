# 선형 검색 알고리즘을 보초법으로 수정

from re import L
from typing import Any, Sequence
import copy

def seq_search(seq : Sequence, key : Any) -> int :
    """시퀀스 seq에서 key와 일치하는 원소를 선형 검색 (보초법)"""
    
    a = copy.deepcopy(seq)                  # seq를 복사
    a.append(key)                           # 보초 key를 추가
    
    i = 0
    
    while True :
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input('원소 수 : '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))
        
    ky = int(input('검색 값 : '))
    
    idx = seq_search(x, ky)
    
    if idx == -1 :
        print('검색 원소 존재 x')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')