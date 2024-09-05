N = int(input())

number_list = list(range(2, 10000 + 1))
prime_list = []

while len(number_list) != 0:
    prime = number_list[0]
    prime_list.append(prime)

    for i in range(prime, 10000 + 1, prime):
        if i in number_list:
            number_list.remove(i)

for i in range(len(prime_list) - 1):
    special_number = prime_list[i] * prime_list[i + 1]

    if N < special_number:
        print(special_number)
        break