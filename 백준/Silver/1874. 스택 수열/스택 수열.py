import sys
input = sys.stdin.readline

N = int(input())

numbers = []
i = 1
st = True
rs = []

for _ in range(N):
    num = int(input())
    if num < i and (not numbers or numbers[-1] != num):
        st = False
        break
    elif numbers and numbers[-1] == num:
        numbers.pop()
        rs.append("-")
    else:
        while i <= num:
            numbers.append(i)
            rs.append("+")
            i += 1
        numbers.pop()
        rs.append("-")

if not st :
    print("NO")
else :
    for r in rs :
        print(r)