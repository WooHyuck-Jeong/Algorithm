# 8퀸 문제 해결 알고리즘

pos = [0] * 8                   # 각 열에 배치한 퀸의 위치
flag_a = [False] * 8            # 각 행에 퀸을 배치했는지 체크 
flag_b = [False] * 15           # 대각선 방향(1, 7시)으로 퀸을 배치했는지 체크
flag_c = [False] * 15           # 대각선 방향(5시 10시)으로 퀸을 배치했는지 체크

def put() -> None:
    """각 열에 배치한 퀸의 위치를 출력"""
    # for i in range(8):
    #     print(f'{pos[i]:2}', end= '')
    # print()
    for j in range(8):
        for i in range(8):
            print('■' if pos[i] == j else '□', end='')  
        print()
    print()
    
def set(i: int) -> None:
    """i열에 알맞은 위치에 퀸을 배치"""
    for j in range(8):
        if (not flag_a[j] 
            and not flag_b[i+j] 
            and not flag_c[i - j + 7]):
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i - j + 7] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i - j + 7] = False

set(0)