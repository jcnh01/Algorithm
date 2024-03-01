import sys

input = sys.stdin.readline()

number = list(map(int, input.strip()))

number.sort(reverse=True)

for i in number:
    print(i, end="")