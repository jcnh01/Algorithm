import sys
input = sys.stdin.readline

N = int(input())

num = [0, 1, 2]

numbers = []

cnt = 0

def dfs() :
    global cnt
    if len(numbers) == N :
        n = ''
        if numbers[0] == 0 :
            return
        for num in numbers :
            n += str(num)
        if int(n) % 3 == 0 :
            cnt += 1
        return
    for i in range(3) :
        numbers.append(i)
        dfs()
        numbers.pop()

dfs()
print(cnt)