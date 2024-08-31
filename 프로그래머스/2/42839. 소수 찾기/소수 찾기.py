from itertools import permutations

def solution(numbers) :
    answer = 0
    num = set()
    
    for i in range(1, len(numbers) + 1) :
        li = list(permutations(numbers, i))
        for l in  li :
            a = ""
            for j in range(len(l)) :
                a += l[j]
            num.add(int(a))
    
    for n in num :
        st = True
        if n == 0 or n == 1 :
            continue
        for i in range(2, n) :
            if n % i == 0 :
                st = False
                break
        if st :
            answer += 1
    
    return answer