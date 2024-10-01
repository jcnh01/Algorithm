import sys
input = sys.stdin.readline
from collections import deque
q = deque()

N = int(input())
graph = [[] for _ in range(28)]

for _ in range(N) :
    a, b, c = map(str, input().split())
    graph[ord(a) - 97].append(ord(c) - 97)

def bfs(c, visit) :
    st = False
    while q :
        num = q.popleft()
        if c == num :
            st = True
            break
        for i in graph[num] :
            if not visit[i] :
                q.append(i)
    return st

M = int(input())
for _ in range(M) :
    a, b, c = map(str, input().split())
    visit = [False] * 28
    q.append(ord(a) - 97)
    rs = bfs(ord(c) - 97, visit)
    if rs :
        print("T")
    else :
        print("F")