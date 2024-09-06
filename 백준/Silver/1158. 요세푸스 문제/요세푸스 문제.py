import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

q = deque()
for i in range(1, N + 1) :
    q.append(i)

i = 0

rs = []

while q :
    i += 1
    num = q.popleft()
    if i != K :
        q.append(num)
    else :
        rs.append(num)
    if i == K :
        i = 0

print("<", end = "")

for i in range(len(rs)) :
    if i == len(rs) - 1 :
        print(rs[i], end = "")
    else :
        print(rs[i], end = "")
        print(",", end = " ")

print(">")