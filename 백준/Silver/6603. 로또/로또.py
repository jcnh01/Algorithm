import sys
input = sys.stdin.readline

def find(num, start, end, arr) :
    if num == end :
        for i in range(num) :
            print(li[i], end = " ")
        print()
        return
    for i in range(start, len(arr)) :
        li.append(arr[i])
        find(num+1, i+1, end, arr)
        li.pop()

while True :
    numbers = list(map(int, input().split()))
    li = []
    if not numbers[0] :
        break
    find(0, 0, 6, numbers[1:])
    print()