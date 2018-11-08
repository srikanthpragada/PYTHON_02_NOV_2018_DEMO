for n in range(1, 11):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    print(f"{n:2d}  {fact}")
