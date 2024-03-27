import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    k = int(input())
    n = int(input())
    lst = [[i for i in range(1, 15)] for _ in range(k+1)]
    i = 1 
    j = 0  
    
    while True:
        j += 1 
        
        lst[i][j-1] = sum(lst[i-1][:j])
        
        if i == k and j == n :
            print(lst[i][j-1])
            break
        
        if j == 14 :
            i += 1
            j = 0 