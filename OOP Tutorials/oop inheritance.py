# Python Object-Oriented Programming Notes
# Brendan Dameworth
# Method Resolution Order - if the employee class was empty it would pass to the next class


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


class Developer(Employee):  # by passing the Employee class to the Developer class, it inherits all attributes
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)   #passes args to Employees init method to handle logic
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer("Brendan", "Dameworth", 50000, 'Python')  # you can create a developer using the developer class (using inherited attributes)
dev_2 = Developer("Test", "User", 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])



# print(issubclass(Manager, Developer))
# print(issubclass(Manager, Developer))

# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


# print(help(Developer))

# print(dev_1.email)
# print(dev_2.email)
