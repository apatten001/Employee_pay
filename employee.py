

class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return "{}{}@company.com".format(self.first, self.last)
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = (self.pay * self.raise_amount)
        return self.pay

emp_2 = Employee("arnold", "patten",200)

print(emp_2.fullname)
print(emp_2.apply_raise())