import sys
input = sys.stdin.readline

N = int(input())

T = []
P = []

dp = [0] * (N + 1)

for _ in range(N):
    A, B = map(int, input().split())
    T.append(A)
    P.append(B)

for i in range(N - 1, -1, -1):
    if i + T[i] <= N:
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])
    else:
        dp[i] = dp[i + 1]

print(dp[0])
