input_data = ["10,James", "20,Bill", "10,Steve", "10,Jason",
              "20,Stepehn", "30,Richards"]
depts = {}
for entry in input_data:
    parts = entry.split(",")
    deptno = parts[0]
    ename = parts[1]
    # find out whether dept no is already present
    if deptno in depts:
        # add new name to existing list
        depts[deptno].append(ename)
    else:
        # Create a new entry with dept no and a list
        depts[deptno] = [ename]

# Dispaly deptno and list of names
for  dno, names in  depts.items():
    print(dno, ",".join(names))
