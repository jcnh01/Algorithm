import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 1

rs = 0

while right <= N and left <= right :
    hap = sum(nums[left:right])

    if hap < M :
        right += 1
    elif hap > M :
        left += 1
    elif hap == M :
        rs += 1
        right += 1

print(rs)