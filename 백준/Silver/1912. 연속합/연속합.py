import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

if N == 1 :
    print(numbers[0])
    quit()

if max(numbers) < 0 :
    print(max(numbers))
    quit()

for i in range(1, N) :
    if i == 1 :
        if numbers[0] > 0:
            numbers[1] += numbers[0]
    else :
        if numbers[i-1] > 0 :
            numbers[i] += numbers[i-1]

print(max(numbers))