N = int(input())

numbers = []

for _ in range(N) :
    num = int(input())
    numbers.append(num)

for _ in range(len(numbers)) :
    print(min(numbers))
    numbers.remove(min(numbers))