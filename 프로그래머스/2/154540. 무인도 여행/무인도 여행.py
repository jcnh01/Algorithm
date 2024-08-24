from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

q = deque()

def bfs(w, d, maps, visit) :
    rs = 0
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    while q :
        y, x = q.popleft()
        rs += int(maps[y][x])
        for i in range(4) :
            Y, X = y + dy[i], x + dx[i]
            if 0 <= Y < d and 0 <= X < w and not visit[Y][X] and maps[Y][X] != 'X' :
                q.append((Y, X))
                visit[Y][X] = True
    return rs

def solution(maps):
    answer = []
    
    visit = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)) :
        for j in range(len(maps[0])) :
            if not visit[i][j] and maps[i][j] != 'X' :
                q.append((i, j))
                visit[i][j] = True
                answer.append(bfs(len(maps[0]), len(maps), maps, visit))
                
    answer.sort()
    
    if not answer :
        return [-1]
    
    return answer