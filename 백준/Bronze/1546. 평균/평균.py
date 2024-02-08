N = int(input())

grade = list(map(int, input().split()))

max = grade[0]

for i in range(1, N) :
    if grade[i] > max :
        max = grade[i]

for i in range(N) :
    grade[i] = grade[i] / max * 100

result = 0

for i in range(N) :
    result = result + grade[i]

print(result / N)