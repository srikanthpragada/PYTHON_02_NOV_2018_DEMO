class Product:
    taxrate = 15

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property  # Getter
    def name(self):
        return self.__name

    @name.setter  # Setter
    def name(self,newname):
        self.__name = newname

    @property     # Getter
    def net_price(self):
        return self.__price + self.__price * Product.taxrate / 100


p = Product("iPhone x", 100000)
p.name = "iPhone X"    # Property name
print(p.net_price, p.name)

