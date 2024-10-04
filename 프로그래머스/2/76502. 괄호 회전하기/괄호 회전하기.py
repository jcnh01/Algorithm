from collections import deque

def solution(s):
    q = deque(s)
    answer = 0
    
    for _ in range(len(s)) :
        stack = []
        a = q.popleft()
        q.append(a)
        st = True
        for i in q :
            if i == "[" or i == "(" or i == "{" :
                stack.append(i)
            elif i == "]" :
                if not stack :
                    st = False
                    break
                word = stack.pop()
                if word != "[" :
                    st = False
                    break
            elif i == "}" :
                if not stack :
                    st = False
                    break
                word = stack.pop()
                if word != "{" :
                    st = False
                    break
            else :
                if not stack :
                    st = False
                    break
                word = stack.pop()
                if word != "(" :
                    st = False
                    break
        if st and not stack :
            answer += 1
    
    return answer