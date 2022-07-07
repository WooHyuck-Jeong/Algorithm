from re import L
from typing import Any, Sequence

def seq_search(a : Sequence , k : Any ) -> str :
    i = 0
    
    while True :
        if i == len(a):
            return -1
        
        if a[i] == k :
            return i
        
        i += 1
       
       
test_list = ['정우혁', '최재하', '윤찬민', '배영우', '정두영', '김동현']       
       
if __name__ == '__main__':
    # num = int(input('원소 수를 입력하세요 : '))
    
    x = [None] * len(test_list)
    
    # for i in range(len(test_list)):
    #     x[i] = str(input(f'x[{i}] : '))
        
    ky = str(input('검색할 이름 : '))
    
    idx = seq_search(test_list, ky)
    
    if idx == -1:
        print('이름이 없습니다.')
    else:
        print(f'검색된 이름은 x[{idx}]에 있습니다.')