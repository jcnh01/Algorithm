import sys
input = sys.stdin.readline

from collections import deque
q = deque()

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

rs = []

for i in graph[1] :
    rs.append(i)

for i in graph[1] :
    for j in graph[i] :
        if j not in rs :
            rs.append(j)

if not rs :
    print(0)
else :
    print(len(rs) - 1)