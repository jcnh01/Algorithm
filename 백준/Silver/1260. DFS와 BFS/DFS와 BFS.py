n, m, v = map(int, input().split())

graph = [[] for i in range (n+1)]

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph :
    i.sort()

visit_dfs = [False] * (n + 1)

def dfs(start) :
    visit_dfs[start] = True
    print(start, end=" ")
    for next in graph[start] :
        if not visit_dfs[next] :
            dfs(next)

from collections import deque

visit_bfs = [False] * (n + 1)

def bfs(start) :
    q = deque()
    q.append(start)
    visit_bfs[start] = True

    while q:
        one = q.popleft()
        print(one, end= " ")
        for next in graph[one] :
            if not visit_bfs[next] :
                q.append(next)
                visit_bfs[next] = True

dfs(v)
print()
bfs(v)