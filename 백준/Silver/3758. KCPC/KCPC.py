import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    n, k, t, m = map(int, input().split())

    cnt = [0] * (n + 1)
    last = [0] * (n + 1)

    grade = [[0] * (k+1) for _ in range(n+1)]

    for l in range(m) :
        i, j, s = map(int, input().split())
        if grade[i][j] <= s :
            grade[i][j] = s
        cnt[i] += 1
        last[i] = l
    
    numbers = [0]

    for i in range(1, n + 1) :
        numbers.append(sum(grade[i]))

    my_grade = numbers[t]
    my_last = last[t]
    my_cnt = cnt[t]

    rs = 1

    for l in range(1, n + 1) :
        if numbers[l] > my_grade :
            rs += 1
        elif numbers[l] == my_grade and my_cnt > cnt[l] :
            rs += 1
        elif numbers[l] == my_grade and my_cnt == cnt[l] and my_last > last[l] :
            rs += 1

    print(rs)