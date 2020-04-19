# Python Object-Oriented Programming Notes
# Brendan Dameworth
# dunder = __

class Employee:

    raise_amt = 1.04  # Class Variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Brendan", "Dameworth", 50000)  # you can create a developer using the developer class (using inherited attributes)
emp_2 = Employee("Test", "User", 60000)


print(len(emp_1))

# print(len('test'))
# print('test'.__len__())

# print(emp_1 + emp_2)



# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

