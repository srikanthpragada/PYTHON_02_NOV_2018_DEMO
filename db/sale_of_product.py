import sqlite3
import sys

try:
    con = sqlite3.connect(r"e:\classroom\python\nov2\catalog.db")
    cur = con.cursor()
    id = int(input("Enter product id    :"))

    # Validate input
    cur.execute("select qoh from products where prodid = ?", (id,))
    product = cur.fetchone()
    if product is None:
        print("Sorry! Product not found!")
        sys.exit(1)

    qs = int(input("Enter quantity sold :"))
    if qs > product[0]:
        print("Sorry! Quantity on hand is insufficient")
        sys.exit(2)

    cur.execute("update products set qoh = qoh - ? where prodid = ?", (qs, id))
    if cur.rowcount == 1:
        print("Updated product details!")
        con.commit()

except Exception as ex:
    print("Error : ", ex)
finally:
    con.close()
