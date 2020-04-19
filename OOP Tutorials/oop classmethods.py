# Python Object-Oriented Programming Notes
# Brendan Dameworth


class Employee:

    num_of_emps = 0
    raise_amount = 1.04  # Class Variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "Full name: {} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # DECORATOR TO MAKE A CLASS METHOD
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod  # from_string is an alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod # static methods don't operate on the instance or the class 
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Brendan", "Dameworth", 50000)
emp_2 = Employee("Test", "User", 60000)

import datetime

my_date = datetime.date(2020, 4, 20)
print(Employee.is_workday(my_date))



# emp_str_1 = "John-Doe-70000"
# emp_str_2 = "Steve-Smith-30000"
# emp_str_3 = "Jane-Doe-90000"

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)


# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
