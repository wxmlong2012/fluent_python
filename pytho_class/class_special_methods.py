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

    # for debugging, logging, meant to be used by developer
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"
    # for end user to use
    def __str__(self):
        return f"{self.fullname()}, {self.email}"

    # add method
    def __add__(self, other):
        return self.pay + other.pay




# Instantiate the class, get instances
emp_1 = Employee("Tom", "Jerry", 30)
emp_2 = Employee("Bill", "Clinton", 50)

# print will try to call __str__ first, if not exist, will call __repr__ instead
print(Employee)
print(emp_1)
# call __repr__ and __str__ special methods
print(repr(emp_1))
print(str(emp_1))
# this will call the __add__ sepcial method
print(emp_1.pay + emp_2.pay)

print(emp_1.__repr__())
print(emp_1.__str__())

# addition for integer is to call the __add__ for integer class.
print(int.__add__(1, 2))
1 + 2
