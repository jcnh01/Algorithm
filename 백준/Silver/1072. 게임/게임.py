import sys
input = sys.stdin.readline

x, y = map(int, input().split())

per = y * 100 // x

s = 1
e = x

st = False

while s <= e :
    mid = (s + e) // 2

    rs = (y + mid) * 100 // (x + mid)

    if rs > per :
        st = True
        e = mid - 1
    else :
        s = mid + 1

if not st :
    print(-1)
else :
    print(e + 1)