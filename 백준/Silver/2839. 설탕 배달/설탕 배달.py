N = int(input())

dp = [5001] * (N+5)

dp[3], dp[5] = 1, 1

for i in range(6, N+1) :
    dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)

if dp[N] == 5002 or dp[N] == 5001 :
    print(-1)
    quit()
else :
    print(dp[N])