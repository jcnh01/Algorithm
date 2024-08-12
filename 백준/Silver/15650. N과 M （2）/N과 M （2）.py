import sys
input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())

numbers = []

for i in range(N) :
    numbers.append(i+1)

li = list(combinations(numbers, M))

for i in range(len(li)) :
    for j in range(len(li[i])) :
        print(li[i][j], end = " ")
    print()