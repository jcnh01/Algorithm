import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = []

for _ in range(N) :
    numbers.append(int(input()))

numbers.sort()

s = 0
e = 0

rs = sys.maxsize

while e < N and s < N :
    if numbers[e] - numbers[s] < M :
        e += 1
    else :
        rs = min(rs, numbers[e] - numbers[s])
        s += 1

print(rs)