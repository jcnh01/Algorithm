def solution(topping):
    answer = 0
    
    dict_a = {}
    dict_b = {}
    
    a = []
    b = topping[:]
    
    for i in topping :
        if i in dict_b :
            dict_b[i] += 1
        else :
            dict_b[i] = 1
    
    i = 0
    
    while i < len(topping) :
        a = topping[i]
        if a in dict_a :
            dict_a[a] += 1
        else :
            dict_a[a] = 1
        
        dict_b[a] -= 1
        if dict_b[a] == 0 :
            dict_b.pop(a)
        
        if len(dict_a) == len(dict_b) :
            answer += 1
            
        i += 1
    
    return answer