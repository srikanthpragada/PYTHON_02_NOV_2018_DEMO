
def is_even(n):
    print("Checking ", n)
    return n % 2 == 0


def is_prime(n):
    """Checks whether a number is prime

    Args:
      n(int) :  number.

    Returns:
       True  : if number is prime
       False : if number is not prime
    """
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    else:
        return True


def is_odd(n):
    print("Checking ", n)
    return n % 2 != 0
