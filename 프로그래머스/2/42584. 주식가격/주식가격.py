from collections import deque

def solution(prices):
    answer = []
    
    q = deque(prices)

    while q :
        num = q.popleft()
        time = 0
        for a in q :
            time += 1
            if num > a :
                break
        answer.append(time)
    
    return answer