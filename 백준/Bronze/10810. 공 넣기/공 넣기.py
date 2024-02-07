a = list(map(int, input().split()))

N = a[0]
M = a[1]

bucket = [0] * N;

for one in range(M) :
    b = list(map(int, input().split()))
    i = b[0]
    j = b[1]
    k = b[2]

    for two in range(i, j + 1) :
        bucket[two-1] = k

for cc in range(N) :
    print(bucket[cc], end=" ")