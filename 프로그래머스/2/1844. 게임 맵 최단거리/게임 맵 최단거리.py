from collections import deque
q = deque()
q.append((0, 0))

def bfs(visit, graph, N, M) :
    while q :
        y, x = q.popleft()
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        for i in range(4) :
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < N and 0 <= Y < M and graph[Y][X] and not visit[Y][X] :
                graph[Y][X] = graph[y][x] + 1
                visit[Y][X] = True
                q.append((Y, X))

def solution(maps) :
    n = len(maps[0])
    m = len(maps)
    visit = [[False] * n for _ in range(m)]
    visit[0][0] = True
    bfs(visit, maps, n, m)
    answer = 0
    if maps[m - 1][n - 1] == 1:
        answer = -1
    else :
        answer = maps[m - 1][n - 1]
    return answer