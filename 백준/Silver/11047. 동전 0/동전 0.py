N, price = map(int, input().split())

li = []

for _ in range(N) :
    num = int(input())
    li.append(num)

li.sort(reverse=True)

result = 0

for money in li :
    if price >= money :
        result += price // money
        price %= money
    
print(result)