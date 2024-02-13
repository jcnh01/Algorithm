N = int(input())

result = []

while (True) :
    for i in range(2, N) :
        if (N % i) == 0 :
            result.append(i)
            N = N // i
            break
    else :
        result.append(N)
        break

if (N != 1) :
    for i in range(len(result)) :
        print(min(result))
        result.remove(min(result))