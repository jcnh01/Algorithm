import sys
input = sys.stdin.readline
from collections import deque

q = deque()

N = int(input())

graph = [[] for _ in range(N)]
for i in range(N) :
    numbers = list(map(int, input().split()))
    for j in range(N) :
        if numbers[j] == 1 :
            graph[i].append(j)

answer = [[0] * N for _ in range(N)]

def bfs(j) :
    visit = [False] * N
    first = 0
    while q :
        num = q.popleft()
        if num == j and first :
            q.clear()
            return True
        first = 1
        for i in graph[num] :
            if not visit[i] :
                visit[i] = True
                q.append(i)
    return False

for i in range(N) :
    for j in range(N) :
        q.append(i)
        st = bfs(j)
        if st :
            answer[i][j] = 1

for i in range(N) :
    for j in range(N) :
        print(answer[i][j], end = " ")
    print()