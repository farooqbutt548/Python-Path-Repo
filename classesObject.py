'''class Students:
    def __init__(self, a, b, c):
        self.fname = a
        self.lname = b
        self.salary = c


farooq = Students('farooq ', 'butt ', 23000)
zaheer = Students('zaheer ', 'irshaad ', 20000)
# print(f'the salary of {farooq.fname + farooq.lname}is {farooq.salary}')
# print(f'the salary of {zaheer.fname + zaheer.lname}is less than farooq is  {farooq.salary-zaheer.salary}')'''

class Laptop:
    def __init__(self, model, price, size, ram, hard):
        self.model = model
        self.price = price
        self.size = size
        self.ram = ram
        self.hard = hard
        self.specification = ram +' * ' +hard

dell = Laptop('E6430', 25000, '17 inch', '8 gb', '250 gb' )
hp = Laptop('h2545', 20000, '17 inch', '4 gb', '500 gb')

# print(dell.model)
# print(dell.price)

# print(f'the diff b/w dell & hp price: {dell.price} : {hp.price}  , ram: {dell.ram} : {hp.ram}')
# print(f' the specification of dell is : {dell.specification}')clear
