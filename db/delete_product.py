import sqlite3

con = sqlite3.connect(r"e:\classroom\python\nov2\catalog.db")
cur = con.cursor()
id = int(input("Enter product id :"))

cur.execute("delete from products where prodid = ?", (id,))
if cur.rowcount == 1:
    print("Deleted Product!")
    con.commit()
else:
    print("Sorry! Product not found!")

con.close()
