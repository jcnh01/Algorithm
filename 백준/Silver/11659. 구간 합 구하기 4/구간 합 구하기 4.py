import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

hap = [0, numbers[0]]

for i in range(1, N) :
    hap.append(hap[i] + numbers[i])

for i in range(M) :
    i, j = map(int, input().split())
    print(hap[j] - hap[i-1])