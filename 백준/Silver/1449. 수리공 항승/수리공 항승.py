import sys
input = sys.stdin.readline

N, L = map(int, input().split())

numbers = list(map(int, input().split()))

st = [False] * (max(numbers) + 1)

for num in numbers :
    st[num] = True

rs = 0

for i in range(max(numbers) + 1) :
    if not st[i] :
        continue
    else :
        for j in range(L) :
            if i + j > max(numbers) : break
            st[i + j] = False
        rs += 1

print(rs)