t = int(input())
for _ in range(t) :
    
    brackets = list(input())
    stack = []
    
    for s in brackets :
        if s == '(' :
            stack.append(s)
        else :
            if not stack :
                print("NO")
                break
            stack.pop()  
    else :
        print("NO" if stack else "YES")