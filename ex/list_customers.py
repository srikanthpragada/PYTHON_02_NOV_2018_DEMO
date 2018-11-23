# take data from customers.txt and display details in the sorted order of name
import re

f = open("customers.txt","rt")
customers = []
for line in f:
    regexp = r"([A-Za-z. ]+)( +)(\d{10})( +)(\w+@\w+)"
    match = re.match(regexp,line)
    if not match is None:
         customers.append( match.groups())  # add tuple to list


for cust in  sorted(customers):
    print(f"{cust[0]:20s}  {cust[2]:10s}  {cust[4]}")




