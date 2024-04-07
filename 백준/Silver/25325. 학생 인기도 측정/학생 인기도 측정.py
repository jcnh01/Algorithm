import sys
input = sys.stdin.readline

n = int(input())
d = dict()
for i in input().split():
    d[i] = 0

for _ in range(n):
    for i in input().split():
        d[i] += 1
        
for i in sorted(d.items(), key=lambda x:(-x[1],x[0])):
    print(*i)