def solution(arr):
    
    cnt = 1
    for a in arr :
        cnt *= a
        
    print(cnt)
    
    answer = 0
    
    for i in range(max(arr), cnt + 1) :
        st = True
        for a in arr :
            if i % a :
                st = False
                break
        if not st :
            continue
        if st :
            answer = i
            break
    
    return answer