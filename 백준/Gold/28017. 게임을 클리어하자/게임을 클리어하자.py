import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = []

for _ in range(N):
    li.append(list(map(int, input().split())))

for i in range(N - 1):
    for j in range(M):
        temp = min(li[i][:j] + li[i][j + 1:])

        li[i + 1][j] += temp

print(min(li[N - 1]))