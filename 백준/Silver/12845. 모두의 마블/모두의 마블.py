import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

numbers.sort()
numbers.reverse()


k = numbers[0] + numbers[1]

result = k
max_num = numbers[0]

for i in range(2, N) :
    result += numbers[i] + max_num

print(result)