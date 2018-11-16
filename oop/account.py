class Account:
    """
    Account class represents an account in a bank
    """
    # Class attribute or static variable
    minbal = 1000

    @staticmethod
    def set_minbal(minbal):
        Account.minbal = minbal

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
        return f"{self.__acno}, {self.__ahname}, {self.__balance}"

    def __eq__(self, other):
        print('__eq__')
        return self.__acno == other.__acno

    def __gt__(self, other):
        return self.__balance > other.__balance

    def __add__(self, other):
        return Account(self.__acno, self.__ahname, self.__balance + other)


Account.set_minbal(2000)  # call static method

a1 = Account(1, "Mr. Larry", 20000)  # Create an object
print(a1.get_balance())

a3 = a1 + 10000  # Deposit
print(a1)
print(a3)

a2 = Account(1, "Mr. Larry", 10000)  # Create an object
# print(id(a1),id(a2))
print(a1 == a2)
print(a1 != a2)
print(a1 < a2)
