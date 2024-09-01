from collections import deque

def solution(begin, target, words):
    answer = 0
    
    q = deque()
    q.append((begin, 0))
    visit = [False] * len(words)
    
    while q :
        word, temp = q.popleft()
        if word == target :
            answer = temp
            break
        for j in range(len(words)) :
            if not visit[j] :
                cnt = 0
                for i in range(len(words[j])) :
                    if words[j][i] != word[i] :
                        cnt += 1
                if cnt == 1 :
                    visit[j] = True
                    q.append((words[j], temp + 1))
    
    return answer