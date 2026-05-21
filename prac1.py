class Employee:
    raise_amt = 1.04
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
        self.pay = int(self.pay *self.raise_amt)

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

print(isinstance(Develpor,Employee))
print(issubclass(Develpor,Employee))