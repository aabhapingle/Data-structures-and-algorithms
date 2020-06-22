class Employee:
    raise_amt = 1.05
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    def function_give_name(self):
        return self.first + self.last
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first ,last,pay)

emp_str1 = "Amy-Santiago-2000"

new_emp_1 = Employee.from_string(emp_str1)

print(new_emp_1.pay)


emp1 = Employee('Jake','Peralta',2000)

#print(emp1.function_give_name())
#print(Employee.function_give_name(emp1))

print(Employee.raise_amt)
print(emp1.raise_amt)

emp1.raise_amt = 2
print(Employee.raise_amt)
print(emp1.raise_amt)

#Employee.raise_amt=3
#print(Employee.raise_amt)
#print(emp1.raise_amt) #this is very important value did not change

class Developer(Employee):
    raise_amt = 5

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Managers(Employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--->',emp.first)

dev_1 = Developer('rosaa','diaz',2000,'pythonn')
dev_2 = Developer('ro','diu',3000,'java')

mgr_1 = Managers('ross','geller',50000,[dev_1])
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
print(mgr_1.print_emp())

print(dev_1.pay)
print(dev_2.prog_lang)

print(isinstance(mgr_1,Developer))

