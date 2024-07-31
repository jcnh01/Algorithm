import sys
while 1 :
    n,k = map(int,sys.stdin.readline().split())
    if n == 0 and k == 0 :
        break
    n_k = n-k
    a = 1
    b = 1
    for i in range(n,max(k,n_k),-1) :
        a *= i
    for i in range(1,min(n_k,k)+1) :
        b *=i
    print(a//b)