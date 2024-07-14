import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    B = list(map(int, input().split()))
    B.sort()

    cnt = 0

    a = 0

    for i in A :
        cnt += a
        for j in range (a, M) :
            if i > B[j] :
                a += 1
                cnt += 1
            else :
                break

    print(cnt)