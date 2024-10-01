import sys
input = sys.stdin.readline

rs = sys.maxsize

N, M = map(int, input().split())

x = []
y = []

for _ in range(M) :
    Y, X = map(int, input().split())
    x.append(X)
    y.append(Y)

x.sort()
y.sort()

rs = 0

for i in range(M) :
    rs += abs(x[i] - x[M // 2])
    rs += abs(y[i] - y[M // 2])

print(rs)