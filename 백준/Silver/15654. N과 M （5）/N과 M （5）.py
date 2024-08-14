N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()

li = []
st = [False] * N

def dfs(n) :
    if len(li) == M :
        for l in li :
            print(l, end = " ")
        print()
        return
    for i in range(len(numbers)) :
        if st[i] :
            continue
        li.append(numbers[i])
        st[i] = True
        dfs(numbers[i])
        li.pop()
        st[i] = False

dfs(numbers[0])