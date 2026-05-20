class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps+=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay *self.raise_amount)

emp_1 = Employee('Ali','Khan', 5000)

print(Employee.num_of_emps)


# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(Employee.__dict__)
# print(emp_1.raise_amount)

