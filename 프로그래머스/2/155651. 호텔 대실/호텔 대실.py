def solution(book_time):
    answer = 0
    for i in range(len(book_time)) :
        b = book_time[i]
        b[0] = b[0].split(":")
        b[0] = int(b[0][0]) * 60 + int(b[0][1])
        b[1] = b[1].split(":")
        b[1] = int(b[1][0]) * 60 + int(b[1][1]) + 10
    
    book_time.sort(key = lambda x : x[1])
    for i in range(len(book_time)) :
        cnt = 1
        for j in range(i + 1, len(book_time)) :
            if book_time[i][1] > book_time[j][0] :
                cnt += 1

        answer = max(answer, cnt)
    return answer