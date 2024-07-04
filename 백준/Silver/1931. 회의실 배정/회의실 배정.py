import sys
input = sys.stdin.readline

N = int(input())

numbers = []

for i in range(N) :
    numbers.append(list(map(int, input().split())))

numbers.sort(key=lambda numbers: numbers[0])
numbers.sort(key=lambda numbers: numbers[1])

finish = numbers[0][1]

rs = 1

for i in range(1, N) :
    if numbers[i][0] >= finish :
        rs += 1
        finish = numbers[i][1]

print(rs)