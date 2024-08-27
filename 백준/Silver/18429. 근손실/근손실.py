import sys
input = sys.stdin.readline

N, K = map(int, input().split())

nums = list(map(int, input().split()))

numbers = []

rs = 0

st = [False] * N

def dfs() :
    global rs
    if len(numbers) == N :
        cnt = 0
        for num in numbers :
            if cnt + num - K < 0 :
                return
            else :
                cnt += num - K
        rs += 1
        return
    for i in range(N) :
        if st[i] :
            continue
        numbers.append(nums[i])
        st[i] = True
        dfs()
        st[i] = False
        numbers.pop()

dfs()
print(rs)