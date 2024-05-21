def solution(s):
    print(s)
    li = list(map(int, s.split()))
    answer = ""
    answer += str((min(li))) + " "
    answer += str((max(li)))
    return answer