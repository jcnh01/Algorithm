def solution(sequence, k):
    answer = []
    s = 0
    e = 0
    x, y = 9999999, 0
    hap = sequence[0]
    while s <= e and e <= len(sequence) :
        if hap == k :
            if abs(x - y) > abs(s - e) :
                x, y = s, e
            e += 1
            if e == len(sequence) :
                break
            hap += sequence[e]
        elif hap < k :
            e += 1
            if e == len(sequence) :
                break
            hap += sequence[e]
        elif hap > k :
            hap -= sequence[s]
            s += 1

    answer.append(x)
    answer.append(y)
    return answer