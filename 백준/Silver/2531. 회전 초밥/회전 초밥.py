import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

num = []

for _ in range(N) :
    num.append(int(input()))

for i in range(k) :
    num.append(num[i])

rs = 0
for i in range(len(num) - k + 1) :
    a = num[i : i + k]
    a = set(a)
    if c not in a :
        rs = max(rs, len(a) + 1)
    else :
        rs = max(rs, len(a))

print(rs)