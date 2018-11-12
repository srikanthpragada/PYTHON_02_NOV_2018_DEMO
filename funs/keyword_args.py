# Keyword only arguments
def fun(*v, n1, n2):
    print(n1, n2)


# Keyword arguments
def fun2(**args):
    print(type(args))
    for k, v in args.items():
        print(k, v)


fun(10,20,n1=10, n2=20)
# fun(10, 20)  # is invalid

fun2(p1=10, p2=20, name="Python")
