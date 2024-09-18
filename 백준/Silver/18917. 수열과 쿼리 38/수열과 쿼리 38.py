import sys 
n = int(input())

a = 0
b = 0

for _ in range(n) :
    data = list(map(int, sys.stdin.readline().split()))
    
    if data[0] == 1 :
        a += data[1]
        b ^= data[1]
    elif data[0] == 2 :
        a -= data[1]
        b ^= data[1]
    elif data[0] == 3 :
        print(a)
    elif data[0] == 4 :
        print(b)