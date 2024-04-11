from collections import deque

n, k = map(int, input().split())

visit = [0] * 100001

def bfs() :
    q = deque()
    q.append(n)

    while q :
        x = q.popleft()
        if x == k :
            print(visit[x])
            break
        for i in (x-1, x+1, x*2) :
            if 0 <= i < 100001 and not visit[i] :
                visit[i] = visit[x] + 1
                q.append(i)

bfs()