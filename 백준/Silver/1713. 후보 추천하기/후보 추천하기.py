import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

numbers = list(map(int, input().split()))

rs = {}

for num in numbers:
    if num not in rs:
        if len(rs) < N :
            rs[num] = 1
        else :
            min_key = min(rs, key = rs.get)
            rs.pop(min_key)
            rs[num] = 1
    else:
        rs[num] += 1

for i in range(len(rs)) :
    print(min(rs), end = " ")
    rs.pop(min(rs))