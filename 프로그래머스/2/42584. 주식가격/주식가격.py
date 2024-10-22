from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices :
        num = prices.popleft()
        cnt = 0
        for p in prices :
            cnt += 1
            if num > p :
                break
            
        answer.append(cnt)
    
    return answer