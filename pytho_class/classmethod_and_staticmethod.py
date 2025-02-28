from datetime import datetime
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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # alternative constructor
    # class method as alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # class method take cls as default, instance method take self as default.
    # static method takes none, it is just a regular method
    @staticmethod
    def is_workday(day: datetime):
        if day.weekday() in (5,6):
            return False
        return True

# Instantiate the class, get instances
emp_1 = Employee("Tom", "Jerry", 30)
emp_2 = Employee("Bill", "Clinton", 50)

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_2.raise_amount)
print(emp_1.raise_amount)

# class method as alternative constructor
emp_3_str = "John-Doe-7000"
emp_3 = Employee.from_string(emp_3_str)
emp_3.pay

# test staticmethod
today_dt = datetime.now()
Employee.is_workday(today_dt)
