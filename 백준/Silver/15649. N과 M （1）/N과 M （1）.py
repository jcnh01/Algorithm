import sys
input = sys.stdin.readline

N, M = map(int, input().split())

rs = []
visit = [False] * (N+1)

def recur(num) :
    if num == M :
        print(' '.join(map(str, rs)))
        return
    for i in range(1, N+1) :
        if visit[i] == False :
            rs.append(i)
            visit[i] = True
            recur(num+1)
            rs.pop()
            visit[i] = False

recur(0)