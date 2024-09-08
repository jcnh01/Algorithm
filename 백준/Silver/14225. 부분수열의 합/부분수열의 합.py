import sys
input = sys.stdin.readline

from itertools import combinations

N = int(input())

numbers = list(map(int, input().split()))

state = [False] * (sum(numbers) + 2)

for i in range(N + 1) :
    li = list(combinations(numbers, i))
    for l in li :
        state[sum(l)] = True

for i in range(1, len(state)) :
    if not state[i] :
        print(i)
        break