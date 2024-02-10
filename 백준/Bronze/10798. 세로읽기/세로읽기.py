list = []

for i in range(5) :
    word = input()
    list.append(word)

max_len = 0

for i in range(5) :
    if (len(list[i]) > max_len) : max_len = len(list[i])

for i in range(5) :
    if (len(list[i]) < max_len) :
        for j in range(len(list[i]), max_len + 1) :
            list[i] = list[i] + " "

for i in range(max_len) :
    for j in range(5) :
        if (list[j][i]) == " " : print("", end="")
        else : print(list[j][i], end="")