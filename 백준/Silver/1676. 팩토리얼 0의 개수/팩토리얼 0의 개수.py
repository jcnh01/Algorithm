N = int(input())

cnt = 0

while 4 < N:
    cnt += N//5
    N = N//5

print(cnt)