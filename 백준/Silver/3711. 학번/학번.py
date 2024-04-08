import sys
input = sys.stdin.readline

for _ in range(int(input())):
    t = (int(input()))
    j, k = 1,2
    arr = []
    for i in range(t):
        arr.append(int(input()))
    if t == 1:
        print(1)
    else:
        while True:
            arr1 = []
            for i in range(t):
                arr1.append(arr[i] % j)
            if t == len(set(arr1)): break
            j += 1
        print(j) 