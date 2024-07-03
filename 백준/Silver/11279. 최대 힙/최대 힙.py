import sys
input = sys.stdin.readline

import heapq

N = int(input())

numbers = []

for _ in range(N) :
    num = int(input())
    if num == 0 :
        if not numbers :
            print(0)
        else :
            print(-heapq.heappop(numbers))
    else :
        heapq.heappush(numbers, -num)