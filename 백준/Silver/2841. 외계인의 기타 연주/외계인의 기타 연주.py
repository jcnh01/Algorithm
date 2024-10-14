import sys
input = sys.stdin.readline
import heapq

N, P = map(int, input().split())

heap = [[] for _ in range(N + 1)]

rs = 0

for _ in range(N) :
    a, b = map(int, input().split())
    if heap[a] :
        num = -heapq.heappop(heap[a])
        if num < b :
            heapq.heappush(heap[a], -num)
            heapq.heappush(heap[a], -b)
            rs += 1
        elif num == b :
            heapq.heappush(heap[a], -num)
        else :
            cnt = 1
            while heap[a] :
                n = -heapq.heappop(heap[a])
                if n < b :
                    heapq.heappush(heap[a], -n)
                    break
                elif n == b :
                    cnt -= 1
                    break
                cnt += 1
            rs += cnt
            heapq.heappush(heap[a], -b)
            rs += 1
    else :
        heapq.heappush(heap[a], -b)
        rs += 1

print(rs)