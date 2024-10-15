import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    n = int(input())
    numbers = list(map(int, input().split()))

    rs = 0

    num = numbers[n - 1]
    for i in range(n - 2, -1, -1) :
        if numbers[i] < num :
            rs += num - numbers[i]
        else :
            num = numbers[i]
    print(rs)