import sys
input = sys.stdin.readline

N, K = map(int, input().split())
level = []
for _ in range(N) :
    level.append(int(input()))

s, e = min(level), max(level) + K

rs = 0

while s <= e :
    mid = (s + e) // 2
    cnt = 0
    for l in level :
        if l < mid :
            cnt += mid - l
    if cnt <= K :
        rs = max(rs, mid)
        s = mid + 1
    else :
        e = mid - 1

print(rs)