import sys
input = sys.stdin.readline

import heapq

N, H, T = map(int, input().split())

height = []

for i in range(N) :
    height.append(-int(input()))

heapq.heapify(height)

i = 0

for _ in range(T) :
    num = heapq.heappop(height)
    if num == -1 :
        heapq.heappush(height, num)
        break
    if -num < H :
        heapq.heappush(height, num)
        break
    a = -num // 2
    heapq.heappush(height, -a)
    i += 1

height = [-h for h in height]

if max(height) >= H :
    print('NO')
    print(max(height))
else :
    print("YES")
    print(i)