from collections import deque

def solution(plans):
    answer = []
    n = len(plans)
    for i in range(n) :
        name, start, end = plans[i]
        hour, minute = start.split(":")
        plans[i] = (name, int(hour) * 60 + int(minute), int(end))
    plans.sort(key = lambda x : x[1])
    
    li = deque()
    for i in range(n) :
        if i == n - 1 :
            answer.append(plans[n - 1][0])
            break
        p = plans[i]
        if p[1] + p[2] <= plans[i + 1][1] :
            answer.append(p[0])
            a = plans[i + 1][1] - p[1] - p[2]
            while a :
                if not li : break
                b = li.pop()
                if b[1] <= a :
                    a -= b[1]
                    answer.append(b[0])
                else :
                    li.append((b[0], b[1] - a))
                    a = 0
        else :
            li.append((p[0], -(plans[i + 1][1] - p[1] - p[2])))
            
    while li :
        a = li.pop()
        answer.append(a[0])
    return answer