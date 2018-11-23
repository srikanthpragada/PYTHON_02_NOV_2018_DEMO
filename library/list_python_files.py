import os

files = os.walk(r"e:\classroom\python\nov2\demo")

for (dirname, directories, files) in files:
    for file in files:
        if file.endswith(".py"):
            print(dirname + "\\" + file)
