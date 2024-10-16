import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

nums = set()
for n in numbers :
    nums.add(n)

sorted_num = sorted(nums, key = lambda x : x)

dic = {}
for i in range(len(sorted_num)) :
    dic[sorted_num[i]] = i
for i in numbers:
    print(dic[i], end = ' ')