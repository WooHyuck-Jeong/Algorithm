from max import max_of

print('End를 입력하면 종료')

number = 0
x = []

while True:
    s = input(f'x[{number}] 값을 입력 :')
    if s == 'End':
        break
    x.append(int(s))
    number += 1
    
print(f'{number}개를 입력하였습니다.')
print(f'최댓값은 {max_of(x)} 입니다.')