import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
result = 0
acc = 0

for i in range(n):
    result += num[i] * acc
    acc += num[i]

print(result)