number = []

for i in range(9) :
    num = list(map(int, input().split()))
    number.append(num)

max = 0
row = 0
column = 0

for i in range (9) :
    for j in range(9) :
        if(number[i][j] > max) :
            max = number[i][j]
            row = i
            column = j

print(max)
print(row+1, column+1)