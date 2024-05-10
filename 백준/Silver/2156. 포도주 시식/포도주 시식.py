n = int(input())

dp = [[0] * 3 for _ in range(n)]

numbers = []

for _ in range(n) :
    numbers.append(int(input()))

dp[0][0], dp[0][1], dp[0][2] = 0, numbers[0], numbers[0]

for i in range(1, n) :
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + numbers[i]
    dp[i][2] = dp[i-1][1] + numbers[i]

print(max(dp[n-1]))