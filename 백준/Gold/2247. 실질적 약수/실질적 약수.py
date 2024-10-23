import sys
input = sys.stdin.readline

n = int(input())

rs = 0

for i in range(2, (n // 2) + 1):
    rs += ((n // i) - 1) * i

print(rs % 1000000)