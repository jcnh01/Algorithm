from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque()
    
    rs = []
    
    for i in range(len(priorities)) :
        q.append((i, priorities[i]))
    
    priorities.sort()
    
    while q :
        num, one = q.popleft()
        if priorities[-1] == one :
            rs.append(num)
            priorities.pop()
        elif priorities[-1] != one :
            q.append((num, one))
    
    return rs.index(location) + 1