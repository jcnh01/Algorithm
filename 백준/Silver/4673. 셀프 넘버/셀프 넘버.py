nums = [i for i in range(1, 10001)]
remove_nums = []

for num in nums:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        remove_nums.append(num)

remove_nums = set(remove_nums)

for r_num in remove_nums:
    nums.remove(r_num)

for num in nums:
    print(num)