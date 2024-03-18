import sys
input = sys.stdin.readline

n = int(input())

a, b = map(int, input().split())

m = int(input())

parent = [[] for _ in range(n+1)]

visit = [0] * (n+1)

for _ in range(m) :
    aa, bb = map(int, input().split())
    parent[aa].append(bb)
    parent[bb].append(aa)

from collections import deque
q = deque()

cnt = 1

result = []

def bfs(a, b) :
    visit[a] = 1
    q.append(a)
    while q :
        now = q.popleft()
        if now == b :
            return visit[b]-1
        for next in parent[now] :
            if not visit[next] :
                q.append(next)
                visit[next] += visit[now] + 1


result.append(bfs(a, b))

if not visit[b] :
    print(-1)
else :
    print(result[0])