import sys
input = sys.stdin.readline

N = int(input())

rs = []

for i in range(N, 1000000) :
    st = True
    k = str(i)
    for j in range(len(str(i)) // 2) :
        if k[j] != k[-j - 1] :
            st = False
            break
    if st :
        if i < 2 :
            st = False
        for l in range(2, i) :
            if not i % l :
                st = False
                break
    if st :
        rs.append(i)
        break

if not rs :
    print(1003001)
else :
    print(rs[0])