def is_even(n):
    print("Checking ", n)
    return n % 2 == 0


def is_odd(n):
    print("Checking ", n)
    return n % 2 != 0


nums = [10, 20, 11, 25, 30]
sel_nums = filter(lambda n: n % 2 == 0, nums)

# print(sel_nums)

for n in sel_nums:
    print(n)
