# Create a class
class Employee:
    # this is a class variable
    raise_amount = 1.04
    # employee number equals zero
    number_of_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
        # here we use Employee (class variable) because for all the instance this number won't change
        Employee.number_of_employee += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        # We set self.raise_amount(this is a class variable, but can be changed for individual instance)
        self.pay = int(self.pay * self.raise_amount)


# Instantiate the class, get instances
emp_1 = Employee("Tom", "Jerry", 30)
emp_2 = Employee("Bill", "Clinton", 50)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # super() is used to initiate the first, last, and pay parameters the same way as Employee
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


dev_1 = Developer("Tom", "Jerry", 30, "python")
dev_1.apply_raise()
dev_2 = Developer("Bill", "Clinton", 50, "java")


print(dev_1.pay)
print(dev_1.prog_lang)
# print(help(Developer))


class Manager(Employee):

    def __init__(self, first, last, pay, employee_list=None):
        super().__init__(first, last, pay)
        if employee_list is None:
            self.employee_list = []
        else:
            self.employee_list = employee_list

    def add_emp(self, emp):
        if emp not in self.employee_list:
            self.employee_list.append(emp)

    def remove_emp(self, emp):
        if emp in self.employee_list:
            self.employee_list.remove(emp)

    def print_employee(self):
        for emp in self.employee_list:
            print("-->", emp.fullname())


mgr_1 = Manager("Sue", "Smith", 100, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.add_emp(emp_1)

print("before removing ...")
mgr_1.print_employee()

mgr_1.remove_emp(dev_1)
print("after removing ...")
mgr_1.print_employee()

# mgr–1 is an instance of Manager and Employee, but not Developer
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

# Developer is a subclass of Employee,  but not of Manager:
print(issubclass(Developer, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))