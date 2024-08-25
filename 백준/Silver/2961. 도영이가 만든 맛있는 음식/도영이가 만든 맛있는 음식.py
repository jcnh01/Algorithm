import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())

numbers = []

for _ in range(N) :
    numbers.append(list(map(int, input().split())))

li = []

for i in range(1, N + 1) :
    a = list(combinations(numbers, i))
    for j in a :
        li.append(j)

rs = sys.maxsize

for l in li :
    a = 0
    b = 1
    for j in range(len(l)) :
        a += l[j][1]
        b *= l[j][0]
    if abs(a - b) < rs :
        rs = abs(a - b)

print(rs)