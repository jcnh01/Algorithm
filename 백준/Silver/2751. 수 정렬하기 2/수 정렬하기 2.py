import sys

a = int(input())

numbers = []

for _ in range(a) :
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for i in range(a) :
    print(numbers[i])