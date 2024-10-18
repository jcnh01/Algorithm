from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    num = []
    for i in range(len(dungeons)) :
        num.append(i)
    
    li = list(permutations(num, len(dungeons)))
            
    for l in li :
        cnt = 0
        a = k
        for i in l :
            if dungeons[i][0] <= a :
                a -= dungeons[i][1]
                cnt += 1
        answer = max(answer, cnt)
    return answer