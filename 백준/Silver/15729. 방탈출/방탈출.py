import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

s = [0] * N
cnt = 0

for i in range(N) :
    if s[i] != numbers[i] :
        for j in range(3) :
            if i + j >= N :
                break
            if s[i+j] :
                s[i+j] = 0
            else :
                s[i+j] = 1
        cnt += 1

print(cnt)