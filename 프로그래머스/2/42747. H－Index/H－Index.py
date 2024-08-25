def solution(citations):
    answer = 0
    
    citations.sort()
    citations.reverse()
    for i in range(len(citations)) :
        if citations[i] < i + 1 :
            return i
    return len(citations)