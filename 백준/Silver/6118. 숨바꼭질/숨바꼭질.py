import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()

q.append((1, 0))

visit = [False] * (N + 1)
visit[1] = True

rs = [0] * (N + 1)

while q :
    num, cnt = q.popleft()
    rs[num] = cnt
    for i in graph[num] :
        if not visit[i] :
            visit[i] = True
            q.append((i, cnt + 1))

max_rs = max(rs)
first = 0
st = False
cnt = 1

for i in range(len(rs)) :
    r = rs[i]
    if r == max_rs and not st :
        first = i
        st = True
    elif st and r == max_rs :
        cnt += 1

print(first, max_rs, cnt)