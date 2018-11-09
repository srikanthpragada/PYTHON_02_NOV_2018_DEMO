st = input("Enter a names separated by comma  :")

names = st.split(",")

for n in names:
    n = n.strip(' ')
    if n.isalpha():
        print("%-15s %2d" % (n , len(n)))



