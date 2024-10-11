import heapq
def solution(n, k, enemy):
    answer = 0
    
    i = 0
    heap = []
    while i < len(enemy) :
        if k :
            heapq.heappush(heap, enemy[i])
            k -= 1
        else :
            num = heapq.heappop(heap)
            if num >= enemy[i] :
                heapq.heappush(heap, num)
                n -= enemy[i]
            else :
                heapq.heappush(heap, enemy[i])
                n -= num
        
        if n < 0 :
            break
        
        i += 1
        answer += 1
    
    return answer