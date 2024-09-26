import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

word = input()

io = "I"

for _ in range(N) :
    io += "OI"

i = 0
rs = 0

while i < M :
    if word[i : i + 2 * N + 1] == io :
        rs += 1
    i += 1

print(rs)