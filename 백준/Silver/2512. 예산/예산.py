import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

numbers.sort()

money = int(input())

s = 1
e = numbers[N-1]

while s <= e :
    mid = (s + e) // 2

    hap = 0

    for num in numbers :
        if num > mid :
            hap += mid
        else :
            hap += num

    if hap > money :
        e = mid - 1
    else :
        s = mid + 1

print(e)