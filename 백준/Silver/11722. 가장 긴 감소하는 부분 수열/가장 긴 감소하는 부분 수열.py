import sys
input = sys.stdin.readline

A = int(input())

numbers = list(map(int, input().split()))

dp = [1] * A

for i in range(A):
    for j in range(0, i):
        if numbers[i] < numbers[j] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))