N = int(input())

distances = list(map(int, input().split()))

prices = list(map(int, input().split()))
    
result = 0

a = prices[0]

result = result + prices[0] * distances[0]

for i in range(1, N-1) :
    if (a > prices[i]) :
        a = prices[i]
    result = result + a * distances[i]
        
print(result)