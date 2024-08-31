import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (N + 1)

num = [0] * (N + 1)

for i in range(len(graph)) :
    graph[i].sort()

q = deque()

q.append(R)
visit[R] = True
cnt = 1

num[R] = cnt

while q :
    x = q.popleft()
    for g in graph[x] :
        if not visit[g] :
            visit[g] = True
            cnt += 1
            num[g] = cnt
            q.append(g)

for i in range(1, N + 1) :
    print(num[i])