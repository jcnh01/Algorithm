import sys

K = int(sys.stdin.readline())
A = []
for _ in range(K):
  N = int(sys.stdin.readline())
  if N != 0:
    A.append(N)
  else:
    A.pop()
  
print(sum(A))