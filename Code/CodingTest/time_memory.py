import time
start_time = time.time()    # 측정 시작

"""시간 측정 예제"""
a = [1, 5, 6, 3, 2]
s = 0

for i in a:
    s += i
print(s)
"""시간 측정 예제"""

end_time = time.time()      # 측정 종료
print("time : ", end_time - start_time)     # 수행시간 출력