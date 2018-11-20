
with open("marks.txt","rt") as f:
    # read all lines one by one
    for line in f:
        parts = line.strip("\n").split(",")
        # skip if two elements not found
        if len(parts) < 2:
            continue
        name = parts[0]
        # convert all marks from str ot int and ignore errors
        marks = []
        for v in parts[1:]:
            try:
                marks.append(int(v))
            except:
                pass

        # If no marks found then ignore
        if len(marks) == 0 :
            average = None
            print(f"{name:20}")
        else:
            total = sum(marks)
            average = total / (len(marks))
            print(f"{name:20} {total:3d}  {average:5.2f}")



