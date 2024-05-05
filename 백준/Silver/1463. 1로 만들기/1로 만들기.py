N = int(input())

dp = [1000001] * (N + 4)

dp[1], dp[2], dp[3] = 0, 1, 1

for i in range(4, N+1) :
    if not i % 6 :
        dp[i] = min(dp[i-1], dp[int(i/2)], dp[int(i/3)]) + 1
    elif not i % 2 :
        dp[i] = min(dp[i-1], dp[int(i/2)]) + 1
    elif not i % 3 :
        dp[i] = min(dp[i-1], dp[int(i/3)]) + 1
    else :
        dp[i] = dp[i-1] + 1

print(dp[N])