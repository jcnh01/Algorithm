import sys
x, y, w, s = map(int, sys.stdin.readline().split())
answer = 0
if 2*w <= s:
    print((x+y) * w)
else:
    smaller = min(x, y)
    answer = smaller * s
    absXY = abs(x-y)
    if w > s:
        if absXY % 2 == 0:
            answer += absXY * s
        else:
            answer += (absXY-1) * s + w
    else:
        answer += absXY * w
    print(answer)