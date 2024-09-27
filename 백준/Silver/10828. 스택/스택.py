import sys
input = sys.stdin.readline
 
n = int(input())

stack = []

for _ in range(n) :
    a = list(map(str, input().split()))
    word = a[0]
    if len(a) == 1 :
        num = 0
    else :
        num = a[1]
    num = int(num)
    if word == "push" :
        stack.append(num)
    elif word == "top" :
        if stack :
            print(stack[len(stack) - 1])
        else :
            print(-1)
    elif word == "size" :
        print(len(stack))
    elif word == "empty" :
        if not stack :
            print(1)
        else :
            print(0)
    else :
        if stack :
            number = stack.pop()
            print(number)
        else :
            print(-1)