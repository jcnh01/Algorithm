N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()

li = []

def dfs() :
    if len(li) == M :
        for l in li :
            print(l, end = " ")
        print()
        return
    for i in range(len(numbers)) :
        li.append(numbers[i])
        dfs()
        li.pop()

dfs()