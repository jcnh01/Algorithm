def solution(k, tangerine):
    answer = 0
    dic = {}
    for t in tangerine :
        if t in dic :
            dic[t] += 1
        else :
            dic[t] = 1
            
    sorted_dic = sorted(dic.items(), key = lambda x : x[1], reverse = True)
    
    amount = 0
    for d in sorted_dic :
        amount += d[1]
        answer += 1
        if amount >= k :
            break
    return answer