n,b = map(int,input().split())
arr = []
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
  remainder = n % b
  arr.append(number[remainder])
  n //= b
  if n == 0:
    break

for i in range(len(arr)-1,-1,-1):
  print(arr[i],end='')