import sys
input = sys.stdin.readline

N = int(input())

numbers = []

for i in range(N) :
    numbers.append(list(map(int,input().split())))

if N == 1 :
    print(numbers[0][0])
    quit()    

numbers[1][0] += numbers[0][0]
numbers[1][1] += numbers[0][0]

if N == 2 :
    print(max(numbers[1]))
    quit()

for i in range(2, N) :
    for j in range(i + 1) :
        if j == 0 :
            numbers[i][0] += numbers[i-1][0]
        elif j == i :
            numbers[i][j] += numbers[i-1][j-1]
        else :
            if numbers[i-1][j] > numbers[i-1][j-1] :
                numbers[i][j] += numbers[i-1][j]
            else :
                numbers[i][j] += numbers[i-1][j-1]

print(max(numbers[N-1]))