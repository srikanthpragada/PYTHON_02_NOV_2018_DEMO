import sqlite3

con = sqlite3.connect(r"e:\classroom\python\nov2\catalog.db")
cur = con.cursor()
name = input("Enter product name   :")
price = int(input("Enter product price :"))
qoh = int(input("Enter product quantity :"))

cur.execute("insert into products(prodname,price,qoh) values(?,?,?)",
            (name, price, qoh))

print(f"Added {cur.rowcount} row(s)")
con.commit()
con.close()
