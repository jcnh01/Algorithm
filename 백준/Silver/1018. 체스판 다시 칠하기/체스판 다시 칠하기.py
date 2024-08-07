import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = []

for i in range(N) :
    word = list(map(str, input().rstrip()))
    words.append(word)

rs = []

for i in range(N - 7) :
    for j in range(M - 7) :
        cnt = 0
        for k in range(8) :
            for l in range(8) :
                if (k + l) % 2 == 0 and words[i+k][j+l] == 'B' :
                    cnt += 1
                elif (k + l) % 2 != 0 and words[i+k][j+l] == 'W' :
                    cnt += 1
        rs.append(cnt)
        rs.append(64 - cnt)

print(min(rs))