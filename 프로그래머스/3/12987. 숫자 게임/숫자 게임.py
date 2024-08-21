def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    st = [False] * len(B)
    num = 0
    
    for i in A :
        one = i
        for j in range(num, len(B)) :
            if st[j] :
                continue
            if B[j] > one :
                st[j] = True
                num = j
                answer += 1
                break
    
    return answer