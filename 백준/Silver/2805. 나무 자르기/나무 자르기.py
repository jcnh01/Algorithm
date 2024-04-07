import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

s, e = 1, max(nums)

while s <= e:
    h = (s + e) // 2
    tmp = 0

    for t in nums:
        if t > h:
            tmp += t - h

    if tmp >= M:
        s = h + 1
    else:
        e = h - 1

print(e)