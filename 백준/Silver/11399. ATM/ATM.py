N = int(input())

times = list(map(int, input().split()))

time = 0
result = 0

for _ in range(N) :
    time = time + min(times)
    result = result + time
    times.remove(min(times))

print(result)