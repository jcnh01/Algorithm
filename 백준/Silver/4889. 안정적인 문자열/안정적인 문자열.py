import sys
input = sys.stdin.readline

i = 1

while True :
    word = input()
    if word[0] == "-" :
        break
    stack = []
    cnt = 0
    word = word[:-1]
    for w in word :
        if w == "{" :
            stack.append(w)
        else :
            if not stack :
                cnt += 1
                stack.append("{")
            else :
                stack.pop()

    cnt += len(stack) // 2
    print(str(i) + ".", str(cnt))
    i += 1