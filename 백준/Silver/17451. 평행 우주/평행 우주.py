import math
import sys

n = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))[::-1]

v_min = v[0]

for i in range(1, n) :
    if v_min == v[i] :
        continue
    elif v_min < v[i] :
        v_min = v[i]
    else :
        m = math.ceil(v_min / v[i])
        v_min = v[i] * m
        
print(v_min)