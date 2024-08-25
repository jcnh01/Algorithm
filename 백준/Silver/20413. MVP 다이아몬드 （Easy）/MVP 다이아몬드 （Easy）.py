import sys
input = sys.stdin.readline

N = int(input())

s, g, p, d = map(int, input().split())

word = list(map(str, input().rstrip()))

now = 0

rs = 0

for i in range(N) :
    if word[i] == 'B' :
        a = s - now - 1
        rs += a
        now = a
    elif word[i] == 'S' :
        a = g - now - 1
        rs += a
        now = a
    elif word[i] == 'G' :
        a = p - now - 1
        rs += a
        now = a
    elif word[i] == 'P' :
        a = d - now - 1
        rs += a
        now = a
    elif word[i] == 'D' :
        rs += d
        now = d

print(rs)