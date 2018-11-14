# Display factorial of the number given on command line
import sys

if len(sys.argv) == 1:
    print("Usage : python factorial.py  number")
    sys.exit(0)  # Stop program


num = int(sys.argv[1])

fact = 1
for i in range(2, num + 1):
    fact *= i

print(f"Factoiral of {num} is {fact}")
