'''class Students:
    def __init__(self, a, b, c):
        self.fname = a
        self.lname = b
        self.salary = c


farooq = Students('farooq ', 'butt ', 23000)
zaheer = Students('zaheer ', 'irshaad ', 20000)
# print(f'the salary of {farooq.fname + farooq.lname}is {farooq.salary}')
# print(f'the salary of {zaheer.fname + zaheer.lname}is less than farooq is  {farooq.salary-zaheer.salary}')'''

'''class Laptop:
    count_instance = 0
    discount_percent = 10
    def __init__(self, model, price, size, ram, hard):
        Laptop.count_instance += 1
        self.model = model
        self.price = price
        self.size = size
        self.ram = ram
        self.hard = hard
        self.specification = ram +' * ' +hard

    def discount (self):
        if self.price > 20000:
            return (f'the original price is {self.price} & after discount : '), self.price-(self.price//100*self.discount_percent)
        else:
            return 'sorry no discount'

dell = Laptop('E6430', 25000, '17"', '8 gb', '250 gb' )
hp = Laptop('h2545', 22000, '17"', '4 gb', '500 gb')
Lenovo = Laptop('L343', 15000, '15"', '4 gb', '250 gb')

# print(dell.model)
# print(dell.price)

print(dell.discount())
print(Lenovo.discount())
hp.discount_percent = 20
print(hp.discount())
print(Laptop.count_instance)

# print(f'the diff b/w dell & hp price: {dell.price} : {hp.price}  ,ram: {dell.ram} : {hp.ram}')
# print(f' the specification of dell is : {dell.specification}')'''





'''class University:

    def __init__(self, department, subject, shift,cgpa ):
        self.department = department
        self.subject = subject
        self.shift = shift
        self.cgpa = cgpa
        self.fee = 40000

farooq = University( input('enter department : '), input('enter subject : '), input('enter Shift : '), input('enter cgpa : ' ))
print(f'Your, department : {farooq.department} , subject : {farooq.subject} , shift : {farooq.shift} , cgpa : {farooq.cgpa} , fee : {farooq.fee}')'''
