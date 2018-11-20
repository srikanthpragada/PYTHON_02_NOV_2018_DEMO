try:
    num = int(input("Enter a number :"))
    result = 100 / num
except ZeroDivisionError:
    print("Sorry! Number cannot be 0")
except Exception  as ex:
    print("Error : ", ex)
else:
    print("Result = ", result)
finally:
    print("** Completed **")

print("*** The  End ***")
