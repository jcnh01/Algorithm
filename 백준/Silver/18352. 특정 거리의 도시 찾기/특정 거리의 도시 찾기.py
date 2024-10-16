import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())

q = deque()
q.append((X, 0))

graph = [[] for _ in range(N + 1)]

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)

visit = [False] * (N + 1)
visit[X] = True
rs = [0] * (N + 1)

while q :
    num, cnt = q.popleft()
    rs[num] = cnt
    for i in graph[num] :
        if not visit[i] :
            visit[i] = True
            q.append((i, cnt + 1))

answer = []

for i in range(1, N + 1) :
    if rs[i] == K :
        answer.append(i)

for a in answer :
    print(a, end = " ")
if not answer :
    print(-1)