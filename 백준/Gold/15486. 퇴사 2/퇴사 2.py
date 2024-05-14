import sys

input = sys.stdin.readline

N = int(input())

T = [0] * (N+1)
P = [0] * (N+1)
dp = [0] * (N+1)

for i in range(1, N+1) :
    T[i], P[i] = list(map(int, input().split()))

for i in range(1, N+1) :
    dp[i] = max(dp[i], dp[i - 1])
    if T[i] + i - 1 <= N :
        dp[T[i] + i - 1] = max(dp[T[i] + i - 1], dp[i - 1] + P[i])

print(max(dp))