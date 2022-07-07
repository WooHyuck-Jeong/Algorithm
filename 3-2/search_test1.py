# seq_search() 함수를 사용하여 실수 검색하기

from search_while import seq_search

print('실수를 검색합니다.')
print('주의 : "End"를 입력하여 종료합니다.')

number = 0
x = []

while True:
    s = input(f'x[{number}] : ')
    if s == 'End':
        break
    x.append(float(s))
    number += 1
    
ky = float(input('검색 값 : '))

idx = seq_search(x, ky)

if idx == -1 :
    print('검색 값의 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 x[{idx}]에 있습니다.')