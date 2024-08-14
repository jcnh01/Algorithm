N, M = map(int, input().split())

numbers = []

def dfs(start) :
    if len(numbers) == M :
        for num in numbers :
            print(num, end = " ")
        print()
        return
    for i in range(start, N + 1) :
        numbers.append(i)
        dfs(i)
        numbers.pop()

dfs(1)