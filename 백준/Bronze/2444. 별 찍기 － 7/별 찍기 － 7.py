N = int(input())

m = 2 * N

for i in range(1,m):
    a = m - 2 * i
    if i > N:
        print(' '*((-a)//2)+'*'*(2*(m-i)-1))
    else:
        print(' '*(a//2)+'*'*(2*i-1))