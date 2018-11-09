nums = []

for i in range(1,6):
    n = int(input("Enter a number :"))
    if n < 0:
        continue

    nums.append(n)


for n in nums[::-1]:
    print(n)
