import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

left = 0
right = 0
lion_count = 0
min_length = 9999999

while right < N:
    if numbers[right] == 1 :
        lion_count += 1

    while lion_count >= K:
        min_length = min(min_length, right - left + 1)
        if numbers[left] == 1 :
            lion_count -= 1
        left += 1

    right += 1

if min_length == 9999999 :
    print(-1)
else:
    print(min_length)