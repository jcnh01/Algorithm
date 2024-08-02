import sys
input = sys.stdin.readline

t = int(input())
def love(m):
    num = str(m)
    lov = str()
    for s in num:
        lov += str(9-int(s))
    result = m * int(lov)
    return result

for _ in range(t):
    n = input().strip()
    Large = 10 ** (len(n)) // 2
    if int(n) > Large:
        print(love(Large))
    else:
        print(love(int(n)))