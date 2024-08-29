def solution(genres, plays):
    dic = {}
    dic_a = {}
    for i in range(len(genres)) :
        g = genres[i]
        if g in dic :
            dic[g] += plays[i]
        else :
            dic[g] = plays[i]
            
        if g not in dic_a:
            dic_a[g] = []
        dic_a[g].append((plays[i], i))
        
    li = sorted(dic.items(), key = lambda x : x[1], reverse = True)
    
    lis = sorted(dic_a.items(), key = lambda x : (x[1], x[0]), reverse = True)
    
    answer = []
    
    for l in li :
        sss = dic_a[l[0]]
        sss.sort(key = lambda x : x[0], reverse = True)
        if len(sss) == 1 :
            answer.append(sss[0][1])
        else :
            answer.append(sss[0][1])
            answer.append(sss[1][1])
   

    
    return answer