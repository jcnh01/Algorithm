import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

N = int(input())

visited = [False] * (N+1)
tree = [[] for _ in range(N+1)]
answer = [0] * (N+1)
  
for i in range(1, N):
    s, e = map(int, input().split())

    tree[s].append(e)
    tree[e].append(s)

def dfs(n):
    
    visited[n] = True

    for i in tree[n]:
        if not (visited[i]):
            answer[i] = n
            dfs(i)
    
dfs(1)

for i in range(2, N+1) :
    print(answer[i])