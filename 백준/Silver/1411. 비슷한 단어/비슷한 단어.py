import sys
input = sys.stdin.readline

N = int(input())

word_list = []

for _ in range(N) :
    word = input()
    dic = {}
    cnt = 1
    for i in range(len(word)) :
        if word[i] not in dic :
            dic[word[i]] = cnt
            cnt += 1
    w = ""
    for i in range(len(word)) :
        w += str(dic[word[i]])

    word_list.append(w)

rs = 0

for i in range(N) :
    for j in range(i+1, N) :
        if word_list[i] == word_list[j] :
            rs += 1

print(rs)