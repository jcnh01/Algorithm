from collections import deque

A = int(input())

for _ in range(A):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    queue = deque((value, idx) for idx, value in enumerate(num))

    count = 0
    while queue:
        current = queue.popleft()
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            count += 1
            if current[1] == M:
                print(count)
                break