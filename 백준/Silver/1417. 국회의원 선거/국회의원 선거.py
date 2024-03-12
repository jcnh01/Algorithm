N = int(input())

vote = list(int(input()) for _ in range(N))

result = 0

while True:
    if vote.count(max(vote)) == 1 and vote.index(max(vote)) == 0:
        break
    else:
        vote[vote.index(max(vote), 1)] -= 1
        vote[0] += 1
        result += 1

print(result)