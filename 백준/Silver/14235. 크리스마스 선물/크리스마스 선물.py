import sys
input = sys.stdin.readline
import heapq

n = int(input())

numbers = []

for _ in range(n) :
    num = list(map(int, input().split()))
    if not num[0] :
        if not numbers :
            print(-1)
        else :
            print(-heapq.heappop(numbers))
    else :
        for i in range(1, len(num)) :
            heapq.heappush(numbers, - num[i])