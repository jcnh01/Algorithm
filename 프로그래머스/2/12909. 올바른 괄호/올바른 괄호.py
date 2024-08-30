def solution(s):
    answer = True
    
    i = 0
    cnt = 0
    
    while i < len(s) :
        if s[i] == "(" :
            cnt += 1
        else :
            cnt -= 1
        if cnt < 0 :
            answer = False
            break
        i += 1
        
    if cnt :
        answer = False

    return answer