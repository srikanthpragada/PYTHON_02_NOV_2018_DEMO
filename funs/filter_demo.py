def is_even(n):
    print("Checking ", n)
    return n % 2 == 0

def is_prime(n):
    for i in range(2,n//2 + 1):
        if n % i == 0:
            return False
    else:
        return True

def is_odd(n):
    print("Checking ", n)
    return n % 2 != 0


nums = [10, 20, 11, 25, 30]
sel_nums = filter(lambda n: n % 2 == 0, nums)
prime_nums = filter(is_prime, nums)

# print(sel_nums)

for n in prime_nums:
    print(n)
