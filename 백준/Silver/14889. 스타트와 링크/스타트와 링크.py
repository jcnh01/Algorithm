import sys
input = sys.stdin.readline

from itertools import combinations
N = int(input())

numbers = []

for _ in range(N) :
    numbers.append(list(map(int, input().split())))

num = []

for i in range(0, N) :
    num.append(i)

li = list(combinations(num, N // 2))

rs = sys.maxsize

for l in li:
    set_a = set(l)
    set_b = list(set(num) - set_a)
    set_a = list(set_a)
    
    sum_a = 0

    for i in range(len(set_a)) :
        for j in range(i, len(set_a)) :
            sum_a += numbers[set_a[i]][set_a[j]] + numbers[set_a[j]][set_a[i]]

    sum_b = 0

    for i in range(len(set_b)) :
        for j in range(i, len(set_b)) :
            sum_b += numbers[set_b[i]][set_b[j]] + numbers[set_b[j]][set_b[i]]

    rs = min(abs(sum_a - sum_b), rs)

print(rs)