import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(input().rstrip())
res = 0

for i in range(n):
    if arr[i] == 'P':
        for j in range(i - k, i + k + 1):
            if -1 < j < n:
                if arr[j] == 'H':
                    arr[j] = '-'
                    res += 1
                    break

print(res)