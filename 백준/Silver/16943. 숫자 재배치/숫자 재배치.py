import sys
input = sys.stdin.readline

A, B = map(int, input().split())

st = [False] * len(str(A))
num = list(str(A))
numbers = []
rs = -1

def dfs():
    global rs
    if len(numbers) == len(num):
        candidate = int(''.join(numbers))
        if candidate < B:
            rs = max(rs, candidate)
        return
    
    for i in range(len(num)):
        if st[i]:
            continue
        if len(numbers) == 0 and num[i] == '0':
            continue
        st[i] = True
        numbers.append(num[i])
        dfs()
        numbers.pop()
        st[i] = False

dfs()
print(rs)
