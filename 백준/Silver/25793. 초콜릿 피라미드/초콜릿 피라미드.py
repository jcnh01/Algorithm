import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    r, c = map(int, input().split())
    choco = r * c

    n = min(r, c) - 1
    a = max(r, c) - n - 1
    choco += 2 * (((n * (n+1) * (2*n + 1)) // 6) + ((a * n * (n+1)) // 2))
    print(choco, choco-n-1)