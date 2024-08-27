import sys
input = sys.stdin.readline

N, K = map(int, input().split())

country = []

for _ in range(N) :
    country.append(list(map(int, input().split())))

country.sort(key = lambda x : (x[1], x[2], x[3]))
country.reverse()

cnt = 0
j = 0

for c in country :
    if c[0] == K :
        break
    cnt += 1
    j += 1

for i in range(j, -1, -1) :
    if country[i][3] == country[i-1][3] and country[i][1] == country[i-1][1] and country[i][2] == country[i-1][2] :
        cnt -= 1
    else :
        break

print(cnt + 1)