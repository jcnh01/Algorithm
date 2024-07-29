import sys
input = sys.stdin.readline

M = int(input())
numbers = [0]
number = list(map(int, input().split()))
for i in range(M) :
    numbers.append(number[i])

N = int(input())
for i in range(N) :
    A, B = map(int, input().split())
    if A == 1 :
        for i in range(1, 100) :
            if B * i > M :
                break
            if numbers[B * i] == 1 :
                numbers[B * i] = 0
            else :
                numbers[B * i] = 1
    else :
        a = 1
        if numbers[B] == 1 :
            numbers[B] = 0
        else :
            numbers[B] = 1
        for i in range(1, 50) :
            if B - i < 1 or B + i > M :
                break
            if numbers[B - i] != numbers[B + i] :
                break
            else :
                if numbers[B - i] == 1 :
                    numbers[B - i] = 0
                    numbers[B + i] = 0
                else :
                    numbers[B - i] = 1
                    numbers[B + i] = 1

for i in range(1, M + 1) :
    print(numbers[i], end = " ")
    if i % 20 == 0 :
        print()