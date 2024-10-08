import sys
input = sys.stdin.readline
import math

N = int(input())
li = [int(input()) for _ in range(N)]
li.sort()

gcd = li[1] - li[0]
for i in range(2,N) :
  gcd = math.gcd(li[i] - li[i-1], gcd)

divisor_li = []
for i in range(2, int(gcd ** 0.5)+1): 
  if gcd % i == 0 :
    divisor_li.append(i)
    divisor_li.append(gcd // i)

divisor_li.append(gcd)
divisor_li=list(set(divisor_li))
divisor_li.sort()

print(*divisor_li)