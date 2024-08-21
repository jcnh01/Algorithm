import heapq

def solution(A,B):
    answer = 0
    heapq.heapify(A)
    B = [-num for num in B]
    heapq.heapify(B)
    
    for _ in range(len(A)) :
        answer += heapq.heappop(A) * -heapq.heappop(B)

    return answer