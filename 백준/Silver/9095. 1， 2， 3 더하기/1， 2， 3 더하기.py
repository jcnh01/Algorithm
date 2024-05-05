N = int(input())

dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11) :
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

result = []

for _ in range(N) :
    num = int(input())
    if num == 1 :
        result.append(1)
    elif num == 2 :
        result.append(2)
    elif num == 3 :
        result.append(4)
    else :
        result.append(dp[num])

for i in range(len(result)) :
    print(result[i])