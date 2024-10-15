import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
N, M = map(int, input().split())

graph = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(M) :
    one, two = map(int, input().split())
    graph[one].append(two)
    graph[two].append(one)

q = deque()
q.append((a, 0))

visit = [False] * (N + 1)

rs = -1
cnt = 0

while q :
    num, cnt = q.popleft()
    if num == b :
        rs = cnt
        break
    visit[num] = True
    for i in graph[num] :
        if not visit[i] :
            visit[i] = True
            q.append((i, cnt + 1))
    cnt += 1

print(rs)