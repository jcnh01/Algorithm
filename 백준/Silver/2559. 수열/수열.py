import sys
input = sys.stdin.readline

N, K = map(int, input().split())

numbers = list(map(int, input().split()))

li = []

num = sum(numbers[0:K])
li.append(num)

for i in range(N - K) :
    num = num - numbers[i] + numbers[i + K]
    li.append(num)

print(max(li))