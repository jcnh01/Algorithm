import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (N + 1)

num = [0] * (N + 1)

num[R] = 1

for i in range(len(graph)) :
    graph[i].sort()

cnt = 2

def dfs(node) :
    global cnt
    visit[node] = True
    for i in graph[node] :
        if not visit[i] :
            num[i] = cnt
            cnt += 1
            dfs(i)

dfs(R)

for i in range(1, N + 1) :
    print(num[i])