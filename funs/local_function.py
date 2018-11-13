g = 100  # Global variable


def f1():
    v1 = 10  # Enclosing variable
    global g
    # g = g + 1
    print("In f1()", g)

    # Local function
    def f2():
        nonlocal v1
        v1 = 100
        print("In f2()", v1, g)

    f2()
    print("Value of v = ", v1, g)
    print("End of f1()")


f1()
print(g)
