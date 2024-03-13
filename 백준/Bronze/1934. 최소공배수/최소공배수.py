N = int(input())

def gcd(a, b):
    a_list = []
    b_list = []

    for i in range(1, a + 1):
        if a % i == 0:
            a_list.append(i)

    for j in range(1, b + 1):
        if b % j == 0:
            b_list.append(j)

    common_factors = set(a_list) & set(b_list)
    return max(common_factors)

def lcm(a, b):
      return int(a * b / gcd(a, b))

result = []

for _ in range(N) :
    a, b = map(int, input().split())
    result.append(lcm(a, b))

for i in range(N) :
    print(result[i])