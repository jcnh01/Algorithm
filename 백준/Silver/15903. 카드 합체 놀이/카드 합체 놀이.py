import sys
input = sys.stdin.readline

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

import heapq

numbers.sort()

for i in range(m) :
    a = heapq.heappop(numbers)
    b = heapq.heappop(numbers)
    numbers.append(a+b)
    numbers.append(a+b)
    heapq.heapify(numbers)

print(sum(numbers))