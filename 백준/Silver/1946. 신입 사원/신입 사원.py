import sys
input = sys.stdin.readline

t = int(input())

for i in range(t) :
    N = int(input())

    numbers = []

    for _ in range(N) :
        numbers.append(list(map(int, input().split())))

    cnt = 0

    numbers.sort(key = lambda x : x[1])

    a = numbers[0][0]

    for i in range(1, N) :
        a = min(a, numbers[i][0])
        if numbers[i][0] > a :
            cnt += 1

    print(N - cnt)