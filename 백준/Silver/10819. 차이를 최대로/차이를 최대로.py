import sys
input = sys.stdin.readline

from itertools import permutations

N = int(input())

numbers = list(map(int, input().split()))

li = list(permutations(numbers, N))

max_result = 0

for i in li :
    rs = 0
    for j in range(N - 1) :
        rs += abs(i[j] - i[j + 1])
    max_result = max(max_result, rs)

print(max_result)