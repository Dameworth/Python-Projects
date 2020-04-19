# Python Object-Oriented Programming Notes
# Brendan Dameworth

class Employee:   
    
    num_of_emps = 0
    raise_amount = 1.04  #Class Variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return 'Full name: {} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Brendan', 'Dameworth', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)

#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)