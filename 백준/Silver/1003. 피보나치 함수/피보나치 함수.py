m = int(input())

numbers = []
for _ in range(m) :
    num = int(input())
    numbers.append(num)

dp = [0] * 40
dp[0], dp[1] ,dp[2] = 0, 1, 1

for i in range(3, 40) :
    dp[i] = dp[i-1] + dp[i-2]

def fibo(n) :
    if n == 0 :
        return 1, 0
    elif n == 1:
        return 0, 1
    else :
        return dp[n-1], dp[n - 1] + dp[n -2]

for i in range(m) :
    result1, result2 = fibo(numbers[i])
    print(result1, result2)