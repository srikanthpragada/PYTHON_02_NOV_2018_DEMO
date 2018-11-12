def fun():
    print("In fun()")


def fun2():
    print("In fun2()")


def print_message(f):
    f()


print_message(fun)
print_message(fun2)
