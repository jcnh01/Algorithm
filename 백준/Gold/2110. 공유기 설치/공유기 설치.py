import sys
input = sys.stdin.readline

N, C = map(int, input().split())

numbers = []

for _ in range(N) :
    num = int(input())
    numbers.append(num)

numbers.sort()

start = 1
end = numbers[-1] - numbers[0]
result = 0

while start <= end :
    mid = (start + end) // 2

    distance = numbers[0]
    cnt = 1

    for i in range(1, N) :
        if numbers[i] >= distance + mid :
            distance = numbers[i]
            cnt += 1
    
    if cnt >= C :
        start = mid + 1
        result = mid
    else :
        end = mid - 1

print(result)