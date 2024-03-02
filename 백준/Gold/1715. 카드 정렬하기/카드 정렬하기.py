import sys
import heapq

N = int(sys.stdin.readline())

numbers = []

for _ in range(N):
  num = int(sys.stdin.readline())
  heapq.heappush(numbers, num)

result = 0

while len(numbers) > 1:
  a = heapq.heappop(numbers)
  b = heapq.heappop(numbers)
  sum = a + b
  result += sum
  heapq.heappush(numbers, sum)

print(result)
