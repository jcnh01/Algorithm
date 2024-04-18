X = int(input()) - 1

sum = 2
idx = 1

while idx <= X :
    idx += sum
    sum += 1

if sum % 2 == 0 :
    print(f"{idx-X}/{sum-(idx-X)}")
else:
    print(f"{sum-(idx-X)}/{idx-X}")