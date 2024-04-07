import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

M = int(input())

targets = list(map(int, input().split()))

numbers.sort()

def find(st, en, target) :
    if st == en :
        if numbers[st] == target :
            print(1, end = " ")
        else :
            print(0, end = " ")
        return 

    mid = (st + en) // 2

    if numbers[mid] < target :
        find(mid+1, en, target)
    else :
        find(st, mid, target)

for i in range(M) :
    find(0, N-1, targets[i])