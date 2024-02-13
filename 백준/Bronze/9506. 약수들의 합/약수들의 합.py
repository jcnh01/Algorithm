result = []

while (True):
    num = int(input())
    div = 0
    li = []
    re = []

    if(num == -1) : break;

    for i in range(1, num) :
        if (num % i) == 0 :
            div = div + i
            li.append(i)
            s = ""
    if (num == div) :
        s += str(num) + " = "
        for i in range(len(li)-1) :
            s += str(li[i]) + " + "
        s += str(li[len(li)-1])
    else :
        s += str(num) + " is NOT perfect."
    result.append(s)

for i in range(len(result)) :
    print(result[i])