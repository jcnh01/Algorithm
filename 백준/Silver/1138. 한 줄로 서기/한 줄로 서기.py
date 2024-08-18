import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))

numbers = []

visit = [False] * (N + 1)

def logic() :
    for i in range(N) :
        cnt = 0
        for j in range(i) :
            if numbers[i] < numbers[j] :
                cnt += 1
        if cnt != num[numbers[i] - 1] :
            return
    for n in numbers :
        print(n, end = " ")
    return

def dfs() :
    if len(numbers) == N :
        logic()
        return
    for i in range(1, N + 1) :
        if visit[i] :
            continue
        numbers.append(i)
        visit[i] = True
        dfs()
        numbers.pop()
        visit[i] = False

dfs()