import sys
input = sys.stdin.readline

N, M = map(int, input().split())

size = list(map(int, input().split()))

size.sort()

li = []

rs = 0

cnt = 0

st = False

for s in size :
    if s == 10 :
        rs += 1

for i in range(len(size)) :
    if st :
        break
    if not size[i] % 10 and size[i] != 10 :
        now = size[i]
        for i in range(size[i] // 10) :
            if cnt == M :
                st = True
                break
            rs += 1
            cnt += 1
            now -= 10
            if now == 10 :
                rs += 1
                break

size.reverse()

for i in range(N) :
    if st :
        break
    if not size[i] % 10 :
        continue
    else :
        for j in range(size[i] // 10) :
            if cnt == M :
                st = True
                break
            rs += 1
            cnt += 1

print(rs)