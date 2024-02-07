bucket = []
bucket2 = []

a = list(map(int, input().split()))

N = a[0]
M = a[1]

bucket = [0] * N

for i in range(N) :
    bucket[i] = i + 1

for i in range(M) :
    b = list(map(int, input().split()))
    aa = b[0]
    bb = b[1]
    for j in range(aa, bb + 1) :
        bucket2.append(bucket[j-1])
    bucket2.reverse()
    for k in range(aa, bb + 1) :
        bucket[k-1] = bucket2[k - aa]
    bucket2.clear()

for i in range(N) :
    print(bucket[i], end=" ")