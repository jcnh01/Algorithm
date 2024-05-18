import sys
input = sys.stdin.readline

N = int(input())

numbers = []

for _ in range(N) :
    num = list(map(int, input().split()))
    numbers.append(num)

for i in range(1, N) :
    numbers[i][0] += min(numbers[i-1][1], numbers[i-1][2])
    numbers[i][1] += min(numbers[i-1][0], numbers[i-1][2])
    numbers[i][2] += min(numbers[i-1][0], numbers[i-1][1])

print(min(numbers[N-1]))