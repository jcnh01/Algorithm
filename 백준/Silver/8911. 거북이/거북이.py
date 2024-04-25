import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    d = 0

    x, y = 500, 500

    x_min, x_max, y_min, y_max = 500, 500, 500, 500

    ctls = input().strip()

    for ctl in ctls:
        if ctl == 'L' :
            if d == 3 :
                d = 0
            else:
                d += 1
        elif ctl == 'R' :
            if d == 0:
                d = 3
            else:
                d -= 1
        elif ctl == 'F' :
            if d == 0 :
                y += 1
            elif d == 1 :
                x -= 1
            elif d == 2 :
                y -= 1
            elif d == 3 :
                x += 1
        elif ctl == 'B' :
            if d == 0 :
                y -= 1
            elif d == 1 :
                x += 1
            elif d == 2 :
                y += 1
            elif d == 3 :
                x -= 1

        if x_min > x :
            x_min = x
        if x_max < x :
            x_max = x
        if y_min > y :
            y_min = y
        if y_max < y :
            y_max = y

    width = abs(x_max - x_min)
    length = abs(y_max - y_min)

    print(width * length)