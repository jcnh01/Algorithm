import sys
input = sys.stdin.readline

M, N = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()

s = 1
e = max(numbers)

while s <= e :
    mid = (s + e) // 2

    total = sum(num // mid for num in numbers)
    
    if total >= M :
        s = mid + 1
    else :
        e = mid - 1

print(e)