def solution(n, times):
    answer = 0
    s, e = min(times), max(times) * n
    while s <= e :
        mid = (s + e) // 2
        cnt = 0
        for t in times :
            cnt += mid // t
        if cnt < n :
            s = mid + 1
        elif cnt >= n :
            answer = mid
            e = mid - 1
    return answer