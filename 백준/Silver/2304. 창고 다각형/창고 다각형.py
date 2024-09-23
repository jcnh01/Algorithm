import sys
input = sys.stdin.readline

N = int(input())

graph = [0] * 1001

max_H = 0
min_L = 1002
max_L = 0

for _ in range(N) :
    L, H = map(int, input().split())
    max_H = max(H, max_H)
    min_L = min(L, min_L)
    max_L = max(L, max_L)
    graph[L] = H

rs = 0
now = graph[min_L]
y = 0

for i in range(min_L, max_L + 1) :
    if graph[i] > now :
        now = graph[i]
    rs += now
    y = i
    if now == max_H :
        break

now = graph[max_L]

for i in range(max_L, min_L - 1, -1) :
    if graph[i] > now :
            now = graph[i]
    if i == y :
        break
    rs += now
    
print(rs)