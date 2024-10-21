import sys
input = sys.stdin.readline

n = int(input())

rs = 0
for i in range(n) :
    rs = rs + n / (n - i)
    
print(rs)