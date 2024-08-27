import sys
input = sys.stdin.readline

from itertools import combinations

N = int(input())

health = list(map(int, input().split()))
joy = list(map(int, input().split()))

li = []

num = []
for i in range(1, N+1) :
    num.append(i)

for i in range(1, N+1) :
    lis = list(combinations(num, i))
    for l in lis :
        li.append(l)

rs = 0

for l in li :
    cnt = 0
    happy = 0
    for i in range(len(l)) :
        if cnt + health[l[i] - 1] > 99 :
            break
        else :
            cnt += health[l[i] - 1]
            happy += joy[l[i] - 1]
    rs = max(happy, rs)

print(rs)