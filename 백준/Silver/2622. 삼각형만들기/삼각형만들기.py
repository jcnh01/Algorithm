import sys
input = sys.stdin.readline

t = int(input())
rs = 0

for i in range(1, t+1) :
    for j in range(i, t+1) :
        k = t - i - j
        if k >= i + j :
            continue
        else :				
            if j > k :
                break
            rs += 1
print(rs)