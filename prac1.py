class Employee:
    raise_amt = 1.04
    num_of_emps = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps+=1
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self,name):
        first, last  = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    
    def apply_raise(self):
        self.pay = int(self.pay *self.raise_amt)

    def __repr__(self):
        return "Employee ('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
        

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True


class Develpor(Employee):
    raise_amt = 1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
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
            print('--->',emp.fullname())
# emp_str_1 = 'John-Doe-7000'
# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(Employee.__dict__)
# print(emp_1.raise_amount)

dev_1 = Develpor('Corey', 'Schafer',5000,'Python')
dev_2 = Develpor('Joker', 'Khan',900,'Java')


mgr_1 = Manager('Sue','Smith',9000, [dev_1])
# print(dev_1.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.prog_lang)

# mgr_1.print_emps()

# emp_1 = Employee('Ali','Don', 5000)
# import datetime
# my_date = datetime.date(2016, 7,11)
# print(Employee.is_workday(my_date))

# print(isinstance(Develpor,Employee))
# print(issubclass(Develpor,Employee)


emp_1 = Employee('Muhammad','Ali',50000)

emp_2  = Employee('Test','Employee',5000)

emp_1.fullname = 'Cory Jong'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.first)
# print(emp_1)
# print(emp_1 + emp_2)
# print(repr(emp_1))
# print(str(emp_1))

# print(len(emp_1))