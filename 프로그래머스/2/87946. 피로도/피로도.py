from itertools import permutations

def solution(k, dungeons):
    li = list(permutations(dungeons, len(dungeons)))
    print(li[0])
    
    answer = []
    
    for l in li :
        a = k
        cnt = 0
        for z in l :
            if z[0] <= a :
                a -= z[1]
                cnt += 1
        answer.append(cnt)
    
    return max(answer)