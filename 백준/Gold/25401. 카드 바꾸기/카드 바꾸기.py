import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
pair = set()

for i in range(n - 1):
    for j in range(i + 1, n) :
        a = (card[j] - card[i]) / (j - i)
        if a - int(a) == 0:
            b = card[j] - a * j
            pair.add((a, b))

rs = []
for a, b in pair :
    change = 0
    for l in range(n):
        if card[l] != a * l + b :
            change += 1
    rs.append(change)

print(min(rs))