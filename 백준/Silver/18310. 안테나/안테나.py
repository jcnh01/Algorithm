import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

print(numbers[(N-1) // 2])