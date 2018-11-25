import sqlite3

con = sqlite3.connect(r"e:\classroom\python\nov2\catalog.db")
cur = con.cursor()
cur.execute("select * from products order by price")
products = cur.fetchall()
print(f"No. of products : {len(products)}")

# for product in products:
#     print(f"{product[0]:3d}  {product[1]:30s}  {product[2]:6d} {product[3]:3d}")


for (id,name,price,qoh) in products:
    print(f"{id:3d}  {name:30s}  {price:6d} {qoh:3d}")

con.close()
