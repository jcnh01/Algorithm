import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

left = 0
right = 0
rs = 0

count = {}

while right < N :
    num = numbers[right]
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

    while len(count) > 2 :
        left_num = numbers[left]
        count[left_num] -= 1
        if count[left_num] == 0 :
            del count[left_num]
        left += 1

    rs = max(rs, right - left + 1)
    right += 1

print(rs)
