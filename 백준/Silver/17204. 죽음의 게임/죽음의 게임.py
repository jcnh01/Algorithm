import sys
input = sys.stdin.readline

N, K = map(int, input().split())

choice = [0] * N

for i in range(N) :
    choice[i] = int(input())

now = 0
cnt = 0

for _ in range(150) :
    if now == K :
        break
    now = choice[now]
    cnt += 1

if cnt == 150 :
    print(-1)
else :
    print(cnt)