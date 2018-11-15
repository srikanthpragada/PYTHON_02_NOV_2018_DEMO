class Account:
    # Class attribute
    minbal = 1000

    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # Object Attributes
        self.__acno = acno
        self.__ahname = ahname
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - Account.minbal >= amount:
            self.__balance -= amount
        else:
            raise ValueError(f"Insufficient Balance --> {self.__balance}")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return  f"{self.__acno}, {self.__ahname}, {self.__balance}"

    def __eq__(self, other):
        return self.__acno == other.__acno


a1 = Account(1, "Mr. Larry", 10000)  # Create an object
print(a1.get_balance())

a2 = Account(1, "Mr. Larry", 10000)  # Create an object
print(id(a1),id(a2))
print (a1 == a2)



