import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

visit_dfs = [False] * (N+1)

for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i) :
    visit_dfs[i] = True
    for next in graph[i] :
        if not visit_dfs[next] :
            dfs(next)

result = 0

for i in range(1, N+1) :
    if not visit_dfs[i] :
        dfs(i)
        result += 1

print(result)