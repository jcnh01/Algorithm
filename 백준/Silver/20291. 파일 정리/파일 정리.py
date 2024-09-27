import sys
input = sys.stdin.readline

N = int(input())

dic = {}

for _ in range(N) :
    word = input()
    a, b = word.split(".")
    b = b[:-1]
    if b in dic :
        dic[b] += 1
    else :
        dic[b] = 1

sorted_dic = sorted(dic.items(), key = lambda x : x[0])
for s in sorted_dic :
    print(s[0], s[1])