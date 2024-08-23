def solution(skill, skill_trees):
    answer = 0
    
    skill = list(map(str, skill.rstrip()))
    
    for s in skill_trees :
        st = True
        j = 0
        for word in s :
            if word in skill and word != skill[j] :
                st = False
                break
            elif word in skill :
                j += 1
                
        if st :
            answer += 1
    
    return answer