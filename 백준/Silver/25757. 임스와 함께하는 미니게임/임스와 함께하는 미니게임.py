import sys
input = sys.stdin.readline

N, M = map(str, input().split())
N = int(N)

name = set()
for i in range(N) :
    name.add(input())

if M == 'Y' :
    print(len(name))
elif M == 'F' :
    print(len(name) // 2)
else :
    print(len(name) // 3)