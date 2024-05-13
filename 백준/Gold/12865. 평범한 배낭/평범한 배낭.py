N, K = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N)]

for i in range(N):
    W, V = map(int, input().split())
    for j in range(K+1):
        if i == 0:
            if W <= j:
                dp[i][j] = V
        else:
            if W <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V)
            else:
                dp[i][j] = dp[i-1][j]
    
print(dp[N-1][K])