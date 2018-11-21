import json
import pickle


class Person:  # derived from object  Person(object)
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def print_details(self):
        print(self.name)
        print(self.email)


# JSON serialization
p = Person("Abc", "abc@gmail.com", 30)
st = json.dumps(p.__dict__)
print(st)

# Binary serialization
b = pickle.dumps(p)  # Pickling
print(type(b))

p2 = pickle.loads(b) # Unpickling
p2.print_details()
