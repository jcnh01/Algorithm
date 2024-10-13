import sys
input = sys.stdin.readline
from collections import deque

word = list(input())
goal = deque(input())
word.pop()
goal.pop()

answer = 0

while goal :
    rs = 1
    for i in range(len(word)) :
        k = 1
        cnt = 1
        if word[i] == goal[0] :
            for j in range(i + 1, len(word)) :
                if k >= len(goal) :
                    rs = max(cnt, rs)
                    break
                if word[j] == goal[k] :
                    k += 1
                    cnt += 1
                    rs = max(cnt, rs)
                else :
                    break
    for _ in range(rs) :
        if not goal : break
        goal.popleft()
    answer += 1

print(answer)