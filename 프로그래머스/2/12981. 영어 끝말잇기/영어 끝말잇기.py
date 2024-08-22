def solution(n, words):
    answer = []
    w = words[0][0]
    li = []
    
    for i in range(len(words)) :
        if words[i] not in li and words[i][0] == w :
            li.append(words[i])
            w = words[i][-1]
        else :
            player = (i % n) + 1
            turn = (i // n) + 1
            answer.append((player, turn))
            break

    if not answer :
        answer.append((0, 0))
    return answer[0]