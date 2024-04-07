K, N = map(int, input().split())

numbers = []

for i in range(K) :
    num = int(input())
    numbers.append(num)

s, e = 1, max(numbers)

while s <= e :
    h = (s+e) // 2
    hap = 0

    for num in numbers :
        hap += num // h

    if hap >= N :
        s = h + 1
    else :
        e = h - 1

print(e)