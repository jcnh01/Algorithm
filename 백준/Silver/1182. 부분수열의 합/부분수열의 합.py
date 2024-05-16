import sys
input = sys.stdin.readline

N, S = map(int, input().split())

numbers = list(map(int, input().split()))

rs = []

cnt = 0

def recur(num, count) :
    global cnt
    if sum(rs) == S and rs :
        cnt += 1
    if num == N :
        return
    for i in range(count, N) :
        rs.append(numbers[i])
        recur(num + 1, i + 1)
        rs.pop()

recur(0, 0)
print(cnt)