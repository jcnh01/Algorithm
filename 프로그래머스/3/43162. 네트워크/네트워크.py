def solution(n, computers):
    
    graph = [[] for _ in range(n)]
    
    answer = 0
    
    for i in range(n) :
        for j in range(n) :
            if computers[i][j] == 1 :
                graph[i].append(j)

    visit = [False] * n
    
    def dfs(i) :
        for j in graph[i] :
            if visit[j] == False :
                visit[j] = True
                dfs(j)

    for i in range(n) :
        if visit[i] == False :
            visit[i] = True
            dfs(i)
            answer += 1
    
    return answer