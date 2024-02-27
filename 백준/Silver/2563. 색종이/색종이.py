N = int(input())
arr = [[0] * 100 for _ in range(100)]

result = 0
for _ in range(N):
  A,B = map(int,input().split())
  for i in range(A, A+10):
    for j in range(B, B+10):
      if arr[i][j] != 1:
        arr[i][j] = 1
        result += 1

print(result)