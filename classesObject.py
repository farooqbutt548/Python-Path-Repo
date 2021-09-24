class Students:
    increment = 1.5
    def __init__(self, a, b, c):
        self.fname = a
        self.lname = b
        self.salary = c
        self.increment = 1.3

    def increase(self):
        self.salary = int(self.salary * Students.increment)


farooq = Students('farooq ', 'butt ', 23000)
zaheer = Students('zaheer', 'irshaad', 20000)
# print(f'the salary of {farooq.fname + farooq.lname}is {farooq.salary}')
print(farooq.salary)
farooq.increase()
print(farooq.salary)