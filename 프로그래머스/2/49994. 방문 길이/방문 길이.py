def solution(dirs):
    answer = 0
    li = []
    x, y = 0, 0
    for i in range(len(dirs)) :
        d = dirs[i]
        if d == 'U' :
            if y == 5 :
                continue
            else :
                if (x, y, x, y + 1) not in li and (x, y + 1, x, y) not in li :
                    li.append((x, y, x, y + 1))
                y += 1
        elif d == 'L' :
            if x == -5 :
                continue
            else :
                if (x, y, x - 1, y) not in li and (x - 1, y, x, y) not in li :
                    li.append((x, y, x - 1, y))
                x -= 1
        elif d == 'R' :
            if x == 5 :
                continue
            else :
                if (x, y, x + 1, y) not in li and (x + 1, y, x, y) not in li :
                    li.append((x, y, x + 1, y))
                x += 1
        elif d == 'D' :
            if y == -5 :
                continue
            else :
                if (x, y, x, y - 1) not in li and (x, y - 1, x, y) not in li :
                    li.append((x, y, x, y - 1))
                y -= 1
    answer = len(li)
    print(li)
    return answer