import sys
input = sys.stdin.readline

R, C = map(int, input().split())

words = []

for i in range(R) :
    words.append(list(map(str, input().rstrip())))

rs = []

for i in range(R) : # 왼쪽 -> 오른쪽
    word = ""
    for j in range(C) :
        if words[i][j] == "#" :
            if len(word) > 1 :
                rs.append(word)
            word = ""
        else :
            word += words[i][j]
    if word and len(word) > 1 :
        rs.append(word)

for i in range(C) : # 왼쪽 -> 오른쪽
    word = ""
    for j in range(R) :
        if words[j][i] == "#" :
            if len(word) > 1 :
                rs.append(word)
            word = ""
        else :
            word += words[j][i]
    if word and len(word) > 1 :
        rs.append(word)

rs.sort()

print(rs[0])