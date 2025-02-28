
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

# Get attributes of the instance
emp_1.pay
emp_1.first
emp_1.last

# call method of the instance
# note that the fullname() automatically take self, here is the instance emp_1, as the first argument
# even though the 'self' is not explicitly pass to it
emp_1.fullname()

# another way to call this function is use the class, but this time we need to explicitly pass an instance
Employee.fullname(emp_1)


# retrieve class attributes
# Here emp_1 and emp_2 do not have attribute raise_amount, it will retrieve it from the class
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

# Here it shows what attributes they have. We can see that emp_1 does not have attribute raise amount
# But class Employee has
print(emp_1.__dict__)
print(Employee.__dict__)

# what if we do the following
emp_1.raise_amount = 1.05
# we will see that only emp_1's value changed, but not the other two. This is because we just created an instance
# attribute which only belongs to emp_1
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)
# we can see that emp_1 has this 'raise_amount' attribute now.
print(emp_1.__dict__)
print(Employee.__dict__)

# if we change the class attribute now
# and we can see that emp2's and class Employee's raise_amount has changed
Employee.raise_amount = 1.06
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

# after we instantiate two instances, the number increment by 2
print(emp_1.number_of_employee)
print(emp_2.number_of_employee)
print(Employee.number_of_employee)