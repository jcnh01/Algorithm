N = int(input())

count = 0

for i in range(N) :
    word = input()
    words = []
    for j in range(len(word)) :
        if (j == len(word)-1) :
            if word[j] in words :
                count = count + 1
                break
            else : break
        if word[j] != word[j+1] :
            if word[j] in words :
                count = count + 1
                break
            words.append(word[j])
    words.clear()

print(N - count)