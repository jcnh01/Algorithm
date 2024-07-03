import sys
input = sys.stdin.readline

import heapq

N = int(input())

numbers = []

for _ in range(N):
    num = int(input().strip())
    if num == 0:
        if not numbers:
            print(0)
        else:
            print(heapq.heappop(numbers)[1])
    else:
        heapq.heappush(numbers, (abs(num), num))