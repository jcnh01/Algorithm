import sys
input = sys.stdin.readline

visit = set()

N = int(input())
numbers = list(map(int, input().split()))
s = int(input())
visit.add(s - 1)
li = []
li.append(s - 1)
while li :
    num = li.pop()
    if num - numbers[num] not in visit and num - numbers[num] >= 0 and num - numbers[num] < N :
        visit.add(num - numbers[num])
        li.append(num - numbers[num])
    if num + numbers[num] not in visit and num + numbers[num] >= 0 and num + numbers[num] < N :
        visit.add(num + numbers[num])
        li.append(num + numbers[num])

print(len(visit))