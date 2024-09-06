import sys
input = sys.stdin.readline

N = int(input())

M = int(input())

if not M :
    print(min(len(str(N)), abs(100-N)))
    quit()

nums = list(map(str, input().split()))

a = str(N).rstrip()
a_cnt = 0

st = True

for i in a :
    if i in nums :
        st = False

if st :
    print(min(len(str(N)), abs(100-N)))
    quit()

if N == 100 :
    print(0)
    quit()

while True :
    st = True
    for i in a :
        if i in nums :
            st = False
            break
    if st :
        break
    a = int(a)
    a += 1
    a = str(a)
    a_cnt += 1
    if a_cnt > 500000 :
        break

b = str(N).rstrip()
b_cnt = 0

while True :
    st = True
    for i in b :
        if i in nums :
            st = False
            break
    if st :
        break
    if int(b) < 0 :
        b_cnt = sys.maxsize
        break
    b = int(b)
    b -= 1
    b = str(b)
    b_cnt += 1
    if b_cnt > 500000 :
        break

print(min(a_cnt + len(a), b_cnt + len(b), abs(100 - N)))