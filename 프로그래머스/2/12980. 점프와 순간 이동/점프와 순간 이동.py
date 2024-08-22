def solution(N):
    ans = 0
    
    while N != 0 :
        if not N % 2 :
            N /= 2
        else :
            ans += 1
            N -= 1

    return ans