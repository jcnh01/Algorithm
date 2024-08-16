import sys
input = sys.stdin.readline

N = int(input())

numbers = []

st = [False] * (N + 1)

def dfs() :
    if len(numbers) == N :
        for i in range(N) :
            print(numbers[i], end = " ")
        print()
        return
    for i in range(1, N + 1) :
        if st[i] :
            continue
        numbers.append(i)
        st[i] = True
        dfs()
        numbers.pop()
        st[i] = False

dfs()