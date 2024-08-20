import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()

li = []

def dfs(start) :
    if len(li) == M :
        for num in li :
            print(num, end = " ")
        print()
        return
    for i in range(start, N) :
        li.append(numbers[i])
        dfs(i)
        li.pop()

dfs(0)