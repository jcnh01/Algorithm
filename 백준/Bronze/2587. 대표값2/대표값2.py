numbers = []

for _ in range(5) :
    num = int(input())
    numbers.append(num)

numbers.sort()

sum = 0

for i in range(5) :
    sum += numbers[i]

print(sum//5)
print(numbers[2])