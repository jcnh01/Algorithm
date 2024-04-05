dp = [1,1]
n = int(input())
if n == 1:
    print(4)
else:
    for i in range(len(dp), n):
        dp.append(dp[-2] + dp[-1])
    print(dp[n-1] * 4 + dp[n-2] * 2)