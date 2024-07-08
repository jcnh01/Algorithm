S = int(input())

cur = 0
i = 1
cnt = 0
while True:

    cur += i
    cnt += 1
    if cur > S :
        cnt -= 1
        break
    elif cur == S :
        break
    i += 1

print(cnt)