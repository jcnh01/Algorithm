def solution(want, number, discount):
    answer = 0
    
    n = len(discount)
    
    dic = {}
    
    for i in range(len(want)) :
        dic[want[i]] = 0
    
    s = 0
    e = 9
    
    for i in range(10) :
        if discount[i] not in dic :
            dic[discount[i]] = 0
        dic[discount[i]] += 1
    
    cnt = 0
    
    while cnt < n - 9 :
        for i in range(len(want)) :
            st = True
            if dic[want[i]] < number[i] :
                st = False
                break
        if st :
            answer += 1
        dic[discount[s]] -= 1
        s += 1
        e += 1
        if cnt == n - 10 :
            break
        if discount[e] in dic :
            dic[discount[e]] += 1
        else :
            dic[discount[e]] = 0
        cnt += 1
    
    return answer