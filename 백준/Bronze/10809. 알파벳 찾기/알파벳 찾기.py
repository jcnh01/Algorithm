word = input()

arr = []
arr2 = []

for i in range(len(word)) :
    arr.append(ord(word[i]))

for i in range(97, 123) :
    if not(i in arr) :
        arr2.append(-1)
    else :
        one = arr.index(i)
        arr2.append(one)

for i in range(len(arr2)) :
    print(arr2[i], end = " ")