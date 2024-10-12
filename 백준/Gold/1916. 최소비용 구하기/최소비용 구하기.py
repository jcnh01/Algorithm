import sys
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M) :
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

s, e = map(int, input().split())

heap = []
heap.append((0, s))

dis = [sys.maxsize] * (N + 1)
dis[s] = 0

while heap :
    w, node = heapq.heappop(heap)
    if w != dis[node] : continue
    for next_w, next_node in graph[node] :
        if w + next_w < dis[next_node] :
            dis[next_node] = w + next_w
            heapq.heappush(heap, [dis[next_node], next_node])

print(dis[e])