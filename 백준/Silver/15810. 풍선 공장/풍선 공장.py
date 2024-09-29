import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

s, e = 0, max(numbers) * M

rs = e

while s <= e :
    mid = (s + e) // 2

    cnt = 0

    for i in range(N) :
        cnt += mid // numbers[i]
    
    if cnt >= M :
        rs = mid
        e = mid - 1
    else :
        s = mid + 1
    
print(rs)