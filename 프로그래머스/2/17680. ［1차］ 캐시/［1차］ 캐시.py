from collections import deque
def solution(cacheSize, cities):
    answer = 0
    
    q = deque()
    
    if not cacheSize :
        return len(cities) * 5
    
    for c in cities :
        c = c.upper()
        if c in q :
            answer += 1
            q.remove(c)
            q.append(c)
        else :
            if len(q) < cacheSize :
                q.append(c)
                answer += 5
            else :
                q.popleft()
                q.append(c)
                answer += 5
    
    return answer