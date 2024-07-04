import sys
input = sys.stdin.readline

N = int(input())

M = int(input())

graph = [[] for i in range(N+1)]

for i in range(M) :
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

visit = [False for i in range(N+1)]

visit[1] = True

rs = 0

def dfs(num) :
    li = graph[num]
    for a in li :
        if not visit[a] :
            global rs
            rs += 1
            visit[a] = True
            dfs(a)

dfs(1)
print(rs)