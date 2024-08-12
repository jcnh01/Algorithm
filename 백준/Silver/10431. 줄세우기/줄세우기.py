import sys
input = sys.stdin.readline

P = int(input())

for k in range(P):
    numbers = list(map(int, input().split()))
    del numbers[0]
    cnt = 0

    for i in range(1, len(numbers)):
        j = i
        while j > 0 and numbers[j-1] > numbers[j]:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            cnt += 1
            j -= 1

    print(k + 1, cnt)