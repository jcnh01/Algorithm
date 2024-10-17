import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

words = [[] for _ in range(N)]

for i in range(N) :
    words[i] = list(map(str, input().split()))
    words[i] = deque(words[i])

answer = list(map(str, input().split()))

for a in answer :
    st = False
    for w in words :
        if not w : continue
        if w[0] == a :
            w.popleft()
            st = True
            break
    if not st :
        break

for w in words :
    if w :
        st = False

if not st:
    print("Impossible")
else :
    print("Possible")