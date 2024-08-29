def solution(record):
    
    answer = []
    
    dic = {}
    for r in record :
        if 'Enter' in r or 'Change' in r:
            state, name, nickname = r.split()
            dic[name] = nickname
    
    for r in record :
        if 'Enter' in r :
            state, name, nickname = r.split()
            answer.append(dic[name] + "님이 들어왔습니다.")
        elif 'Leave' in r :
            state, name = r.split()
            answer.append(dic[name] + "님이 나갔습니다.")
    
    return answer