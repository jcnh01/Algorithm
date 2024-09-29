import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

s, e = 0, N - 1

rs = sys.maxsize

li = []

while s < e :
    a = numbers[s] + numbers[e]
    if abs(a) < rs :
        li = [numbers[s], numbers[e]]
        rs = abs(a)
    if a < 0 :
        s += 1
    else :
        e -= 1
    
print(li[0], li[1])