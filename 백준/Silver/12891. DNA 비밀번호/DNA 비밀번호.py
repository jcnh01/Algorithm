import sys
input = sys.stdin.readline

q, p = map(int, input().split())

words = list(map(str, input().rstrip()))

A, C, G, T = map(int, input().split())

a, c, g, t = 0, 0, 0, 0

for i in range(p) :
    if words[i] == "A" :
        a += 1
    if words[i] == "C" :
        c += 1
    if words[i] == "G" :
        g += 1
    if words[i] == "T" :
        t += 1

rs = 0

s = 0
e = p-1

while True :
    if A <= a and C <= c and G <= g and T <= t :
        rs += 1

    if e == q - 1 :
        break

    if words[s] == "A" :
        a -= 1
    if words[s] == "C" :
        c -= 1
    if words[s] == "G" :
        g -= 1
    if words[s] == "T" :
        t -= 1
    
    s += 1
    e += 1

    if words[e] == "A" :
        a += 1
    if words[e] == "C" :
        c += 1
    if words[e] == "G" :
        g += 1
    if words[e] == "T" :
        t += 1

print(rs)