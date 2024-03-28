import sys
input = sys.stdin.readline

N = int(input())

A = []

for i in range(N) :
    a = list(map(int, input().split()))
    A.append(a)

B = []

for i in range(N) :
    b = list(map(int, input().split()))
    B.append(b)

result = []

def func() :
    cnt = 0
    for i in range(N) :
        one = A[i]
        two = B[i]
        for j in range(len(A[i])) :
            if one[j] != two[j] :
                cnt += 1
    return cnt

result.append(func())

# 회전 - 2번
def rotate() :
    rows = []
    for i in range(N) :
        row = A[i]
        rows.append(row)
    AA = [[] for _ in range(N)]
    for i in range(N) :
        for j in range(i, N) :
            AA[i].append(rows[j][i])
    AA.reverse()
    for i in range(N) :
        A[i] = AA[i]

rotate()

result.append(func())

rotate()

result.append(func())

# 대칭 - 대칭한 다음 회전 2번 또 진행
for i in range(N) :
    row = A[i]
    row.reverse()

result.append(func())

rotate()

result.append(func())

rotate()

result.append(func())

print(min(result))