def rev(num) :
    num_str = str(num)
    reserved_str = num_str[::-1]
    return int(reserved_str)

a, b = map(int, input().split())

print(rev(rev(a) + rev(b)))