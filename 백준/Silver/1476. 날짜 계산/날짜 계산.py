E, S, M = map(int,input().split())

i, j, k = 0, 0, 0
year = 0

while True:
    i += 1
    j += 1
    k += 1
    year += 1

    if E == i and S == j and M == k:
        break

    if i == 15:
        i = 0
    if j == 28:
        j = 0
    if k == 19:
        k = 0

print(year)