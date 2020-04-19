# Python Object-Oriented Programming Notes
# Brendan Dameworth

class Employee:   
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return 'Full name: {} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp_1 = Employee('Brendan', 'Dameworth', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

emp_1.fullname()
print(Employee.fullname(emp_1))

