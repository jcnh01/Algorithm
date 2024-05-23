N = int(input())

hansu = 0 

for i in range(1,N+1):
    if i < 100:
        hansu += 1
    else:
        hundup = list(map(int,str(i)))
        if hundup[2] - hundup[1] == hundup[1] - hundup[0]:
            hansu += 1

print(hansu)