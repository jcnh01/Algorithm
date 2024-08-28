import sys
input = sys.stdin.readline

from itertools import combinations

def solution(elements):
    n = len(elements)
    answer = 0
    
    s = set()
    
    elements += elements
    for i in range(n) :
        for j in range(n + 1) :
            a = elements[j:i+j]
            s.add(sum(a))
    answer = len(s)
    
    return answer