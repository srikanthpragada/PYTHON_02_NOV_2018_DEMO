class Person:  # derived from object  Person(object)
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_details(self):
        print(self.name)
        print(self.email)

    def change_email(self, newemail):
        self.email = newemail


class Student(Person):
    def __init__(self, name, email, course):
        Person.__init__(self, name, email)
        self.course = course

    def print_details(self):
        Person.print_details(self)
        print(self.course)

    def change_course(self, newcourse):
        self.course = newcourse


class Employee(Person):
    def __init__(self, name, email, job):
        Person.__init__(self, name, email)
        self.job = job

    def print_details(self):
        Person.print_details(self)
        print(self.job)

    def change_job(self, newjob):
        self.job = newjob


# Multiple inheritance
class EmployeeAndStudent(Employee, Student):
    def __init__(self, name, email, course, job):
        Student.__init__(self, name, email, course)
        Employee.__init__(self, name, email, job)
        # self.job = job

    def print_details(self):
        Student.print_details(self)
        print(self.job)


# p = Person("Abc", "abc@gmail.com")
# s = Student("Steve", "steve@gmail.com", "Python")
# s.change_email("steve@abc.com")
# s.print_details()
#
#
# e = Employee("Mike", "mike@gmail.com", "Python Programmer")
# e.change_job("Django Developer")
# e.print_details()

es = EmployeeAndStudent("Bill", "bill@gmail.com", "Angular", "Python Programmer")
print(EmployeeAndStudent.__mro__)
es.change_email("bill@abc.com")
es.print_details()
