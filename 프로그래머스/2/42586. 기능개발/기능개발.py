from collections import deque

def solution(progresses, speeds):
    answer = []
    
    q = deque(progresses)
    s_q = deque(speeds)
    
    rs = []

    while q :
        cnt = 0
        st = False
        for i in range(len(q)) :
            q[i] += s_q[i]
        while q and q[0] >= 100 :
            q.popleft()
            s_q.popleft()
            cnt += 1
            st = True
        if st :
            rs.append(cnt)
    
    return rs