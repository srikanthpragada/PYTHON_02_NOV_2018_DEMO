def change(v):
    v = 0


def add_name(names, name):
    names.append(name)


a = 100
change(a)   # pass by value - cannot change actual param by changing formal param
print(a)

lst = ["Abc"]
add_name(lst, "Xyz")   # Pass by ref - changes actual param by changing formal param
print(lst)
