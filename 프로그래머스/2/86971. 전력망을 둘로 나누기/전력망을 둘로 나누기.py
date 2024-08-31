from collections import deque
q = deque()

def solution(n, wires):
    
    answer = 9999999
    cnt = 0
    
    for i in range(len(wires)) :
        visit = [False] * (n+1)
        graph = [[] * (n+1) for _ in range(n+1)]
        for j in range(len(wires)) :
            if i == j :
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)
                
        print(graph, j)
                
        q.append(a)
        visit[a] = True
            
        rs = 0
        while q :
            x = q.popleft()
            rs += 1
            for num in graph[x] :
                if not visit[num] :
                    visit[num] = True
                    q.append(num)
        aa = abs((n - rs) - rs)
                    
        answer = min(answer, aa)
    
    return answer