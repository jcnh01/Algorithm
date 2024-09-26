import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

visit = [False] * N

j = 0
cnt = 1
rs = []

for i in range(N - 1) :
    visit[j] = True
    rs.append(j + 1)
    cnt += 1
    a = numbers[j]
    if a > 0 :
        while True :
            j += 1
            if j == N :
                j = 0
            if not visit[j] :
                a -= 1
            if not a :
                break
    else :
        while a :
            j -= 1
            if j == -1 :
                j = N - 1
            if not visit[j] :
                a += 1
            if not a :
                break

for i in range(N) :
    if not visit[i] :
        rs.append(i+1)
        break

for r in rs :
    print(r, end = " ")