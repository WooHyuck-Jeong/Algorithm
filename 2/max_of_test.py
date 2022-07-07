# 각 배령 원소의 최댓값을 구해서 출력하기(tuple, string, string list)

from max import max_of

t = (4, 7, 5.6, 2, 3.14, 1)     # tuple
s = 'string'                    # string
a = ['DTS', 'AAC', 'FLAC']      # string list

print(f'{t}의 최댓값은 {max_of(t)}')
print(f'{s}의 최댓값은 {max_of(s)}')
print(f'{a}의 최댓값은 {max_of(a)}')