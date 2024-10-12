import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

s = e = 0

dic = {}
dic[numbers[s]] = 1
rs = 1

while e < N :
    rs = max(rs, e - s)
    e += 1
    if e == N :
        break
    if numbers[e] in dic :
        dic[numbers[e]] += 1
    else :
        dic[numbers[e]] = 1
    if dic[numbers[e]] > K :
        while True :
            dic[numbers[s]] -= 1
            s += 1
            if dic[numbers[e]] <= K :
                break

print(rs + 1)