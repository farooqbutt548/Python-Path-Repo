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
    total_marks = 1100

    def __init__(self, department, subject, shift,cgpa ):
        self.department = department
        self.subject = subject
        self.shift = shift
        self.cgpa = cgpa

        if subject == 'BS-IT':                  # we use if else in attribute
            self.fee =35000
        elif subject == 'BS-SE':
            self.fee = 40000
        elif subject == 'BS-CS':
            self.fee = 30000
        else:
            self.fee = 'enter correct Subject'


farooq = University( input('enter department : '), input('enter subject : '), input('enter Shift : '), input('enter cgpa : ' ))

# print(f'Your, department : {farooq.department} , subject : {farooq.subject} , shift : {farooq.shift} , cgpa : {farooq.cgpa} , fee : {farooq.fee}')

print(f'Your Subject is "{farooq.subject}"')
print(f'Your Shift is "{farooq.shift}"')
print(f'Your CGPA is "{farooq.cgpa}"')
print(f'Your Fee is "{farooq.fee}"')

# print(farooq.total_marks)       # class's variable/attribute, object derieved from class (Inheretance)
# print(University.total_marks)       # class's variable/attribute'''



'''class University:
    total_marks = 1100

    def __init__(self, department, subject, shift,cgpa ):
        self.department = department
        self.subject = subject
        self.shift = shift
        self.cgpa = cgpa
        self.fee = 40000

    @classmethod
    def string_argu(cls, string):
        department, subject, shift, cgpa = string.split(',')
        return cls(department, subject, shift, cgpa)

    @staticmethod
    def intro():
        return f'Hi I am Farooq Butt'

touseef = University.string_argu('ICT,BS-IT,Evening,3.57')      # object arguments paased via a string with class method

print(f'Hi Dear your Department : {touseef.department} .')
print(f'Hi Dear your Subject : {touseef.subject} .')
print(f'Hi Dear your Shift : {touseef.shift} .')
print(f'Hi Dear your CGPA : {touseef.cgpa} .')

print(University.intro())       # this is static method (instance/class independent)
print(touseef.intro())       # this is static method (instance/class independent)'''



'''class Phone:
    def __init__(self, name, model, price):
        self.name = name
        self._model = model
        self.__price = max(price, 0)    # if price negative it will assume zero 

ph1 = Phone('techno', 'spark_5', 18000)
print(ph1.name)
print(ph1._model)
# print(ph1.__price)  # mangling name error 
print(ph1._Phone__price)        # in case of mangling we concatinate _ClassName then mangling attribute
ph1._Phone__price =-18500
print(ph1._Phone__price)    # in mangling Python changes it's name 


class latest_phone(Phone):              # inheritance
    def __init__(self, name, model, price, pixel, size):
        super().__init__(name, model, price)
        self.pixel = pixel
        self.size = size

ph2 = latest_phone('infinix', 'camon 11', 20000, '8 mpx', '8 inch' )

print(f"the old phone's properties is {ph1.name}, {ph1._model}, {ph1._Phone__price} ")
print(f"the latest phone's properties is Name: {ph2.name},Model: {ph2._model},Price: {ph2._Phone__price}, Pixel: {ph2.pixel}, Size: {ph2.size} ")'''