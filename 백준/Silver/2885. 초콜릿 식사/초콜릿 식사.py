import sys
input = sys.stdin.readline

N = int(input())

numbers = []

for i in range(21):
    numbers.append(2 ** i)

size = 0

for i in range(21):
    if N <= numbers[i]:
        size = numbers[i]
        break

if N in numbers:
    print(size, 0)
    quit()

rs = 0
cnt = 0

c = size

while True:
    if cnt + c > N:
        c //= 2
        rs += 1
    else:
        cnt += c

    if cnt == N:
        break

print(size, rs)
