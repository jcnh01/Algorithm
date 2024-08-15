import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

numbers.sort()

s = 0
e = N - 1

rs = sys.maxsize

while s < e :
    if abs(numbers[e] + numbers[s]) <= rs :
        rs_s = numbers[s]
        rs_e = numbers[e]
        rs = abs(numbers[e] + numbers[s])
    if numbers[e] + numbers[s] < 0 :
        s += 1
    elif numbers[e] + numbers[s] > 0 :
        e -= 1
    else :
        break

print(rs_s, rs_e)