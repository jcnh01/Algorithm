N, M = map(int, input().split())

numbers = []

def dfs() :
    if len(numbers) == M :
        for num in numbers :
            print(num, end = " ")
        print()
        return
    for i in range(1, N + 1) :
        numbers.append(i)
        dfs()
        numbers.pop()

dfs()