number = int(input())

numbers = []

for _ in range(number) :
    number = list(map(int, input().split()))
    numbers.append(number)

numbers.sort(key = lambda x: (x[0], x[1]))

for num in numbers :
    print(num[0], num[1])