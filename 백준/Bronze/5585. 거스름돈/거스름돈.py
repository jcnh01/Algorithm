a = 1000 - int(input())
result = 0
bills = [500, 100, 50, 10, 5, 1]

for i in bills:
    if a >= i:
        result += a // i
        a %= i

print(result)