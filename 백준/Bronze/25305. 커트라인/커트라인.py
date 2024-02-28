a = list(map(int, input().split()))

scores = list(map(int, input().split()))
scores.sort()

for i in range(a[1] - 1) :
    scores.remove(max(scores))

print(max(scores))