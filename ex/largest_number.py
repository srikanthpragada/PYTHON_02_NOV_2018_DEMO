largest = 0
i = 1
while i <= 5:
    num = int(input("Enter a number :"))
    if num < 0:
        continue

    i += 1
    if num > largest:
        largest = num

print("Largest = ", largest)
