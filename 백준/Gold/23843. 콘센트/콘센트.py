import sys
input = sys.stdin.readline

import heapq

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers = [-num for num in numbers]
heapq.heapify(numbers)

li = [0] * M

while numbers :
    num = heapq.heappop(numbers)
    index = li.index(min(li))
    li[index] -= num
    
print(max(li))