import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

numbers.sort()

num_dict = {}

for num in numbers :
    if num_dict.get(num) == None :
        num_dict[num] = 1
    else :
        num_dict[num] += 1

for target in targets :
    if num_dict.get(target) == None :
        print(0, end = " ")
    else :
        print(num_dict[target], end = " ")