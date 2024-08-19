import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num = list(map(int, input().split()))

numbers = []

rs = 0

def dfs() :
    global rs
    if len(numbers) == n :
        for j in range(m) :
            if not num[j] in numbers :
                return
        rs += 1
        return
    for i in range(10) :
        numbers.append(i)
        dfs()
        numbers.pop()

dfs()
print(rs)