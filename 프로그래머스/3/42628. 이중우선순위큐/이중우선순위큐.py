import heapq

def solution(operations):
    heap = []
    
    for op in operations :
        word, num = op.split()
        num = int(num)
        
        if word == "I" :
            heapq.heappush(heap, num)
        elif not heap :
            continue
        elif word == "D" :
            if num == -1 :
                heapq.heappop(heap)
            elif num == 1 :
                heap = [-a for a in heap]
                heapq.heapify(heap)
                heapq.heappop(heap)
                heap = [-a for a in heap]
                heapq.heapify(heap)
                
    if not heap :
        return [0, 0]
    else :
        return [max(heap), min(heap)]