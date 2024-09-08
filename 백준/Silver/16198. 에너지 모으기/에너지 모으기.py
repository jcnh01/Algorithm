from itertools import permutations

import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

num = []
for i in range(1, N - 1) :
    num.append(i)

li = list(permutations(num, N - 2))

rs = 0

for l in li :
    visit = [False] * N
    a = 0
    for i in range(len(l)) :
        visit[l[i]] = True
        left = l[i] - 1
        right = l[i] + 1
        while True :
            if visit[left] :
                left -= 1
            if visit[right] :
                right += 1
            if not visit[left] and not visit[right] :
                break
        a += numbers[left] * numbers[right]
    rs = max(rs, a)

print(rs)