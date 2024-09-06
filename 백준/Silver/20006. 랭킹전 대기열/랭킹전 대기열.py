import sys
input = sys.stdin.readline

p, m = map(int, input().split())

room = [[] for _ in range(p)]
owner = [0] * p

for _ in range(p) :
    level, id = map(str, input().split())
    level = int(level)
    st = False
    for i in range(len(owner)) :
        if len(room[i]) < m and owner[i] != 0 :
            if owner[i] - 10 <= level and owner[i] + 10 >= level :
                room[i].append((level, id))
                st = True
                break
    if not st :
        for i in range(len(owner)) :
            if owner[i] == 0 :
                room[i].append((level, id))
                owner[i] = level
                break

for r in room :
    r.sort(key = lambda x : x[1])

for r in room :
    if len(r) == 0 :
        break
    if len(r) == m :
        print("Started!")
    elif len(r) != m :
        print("Waiting!")
    for i in range(len(r)) :
        print(r[i][0], r[i][1])