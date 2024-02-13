N = int(input())

number = list(map(int, input().split()))

result = 0

b = []

for i in range(N) :
    a = number[i]
    if (a == 1) :
        result += 1
    else :
        for j in range(2, a) :
            if (a % j) == 0 :
                result += 1
                b.append(a)
                break

print(N - result)