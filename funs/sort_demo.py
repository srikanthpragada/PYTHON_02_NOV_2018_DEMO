def get_length(s):
    return len(s)


names = ["Java", "c", "python", "C#", "SQL", "cobol"]
ages = {'Abc' : 30,'Pqr' :20, 'Def' : 40, 'Ced' : 39}

# for n in sorted(names):
#     print(n)

# for n in sorted(names, key=str.upper):
#     print(n)

for k,v in sorted(ages.items()):
    print(k,v)

for k,v in sorted(ages.items(), key = lambda t : t[1] ):
    print(k,v)

