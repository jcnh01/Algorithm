from collections import deque
q = deque()
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    
    for i in range(n - 1, -1, -1) :
        while q and q[-1] <= numbers[i] :
            q.pop()
        
        if q :
            answer[i] = q[-1]
        
        q.append(numbers[i])

    return answer