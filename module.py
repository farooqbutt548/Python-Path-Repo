                           # -------------------    Modules 
#          ---------type(1)

# addition and subtraction simple module add(), sub()
'''import module1              # simple module name
print(module1.add(3,4))
print(module1.sub(8,4))

# Febonacci Sequance n-number module    febonacci()
n_num = int(input('enter a digit for n-number febunacci: '))
febu_cell = module1.febonacci(n_num)
print(febu_cell)

# nth addition number n_add()
addition_cell = module1.n_add(10)
print(addition_cell)'''

#          ---------type(2)

'''import module1 as m         # alias name as you like to use

# nth-addition 
addition_cell = m.n_add(10)         # here we use m instead of module1
print(addition_cell)

# Febunacci 
febu_num = m.febonacci(10)
print(febu_num)

# addition and subtraction
print(m.add(7,2))
print(m.sub(7,2))'''

        # -------- type(3)

'''from module1 import add, febonacci, n_add

print(n_add(6))
print(febonacci(10))
print(add(10,8))            # sub is not mentioned so it will not work (when we put some function it auto imported)'''

        # --------type(4)

'''from module1 import n_add as n, febonacci as f

print(n(10))        # now n is equal to n_add in module1
print(f(10))        # now f is equal to febunacci in module1'''

        # ------type(5)
'''from module1 import *

print(add(2,7))
print(sub(2,7))
print(febonacci(12))
print(n_add(50))'''

        #------type(6)

'''from module1 import ab, cd
print(cd(8,2))      # here module1 will execute bcz it does know that module2 is coming next
from module2 import ab, cd
#  if 2 different modules have same variablr, functio or method then last mention module has most periority

print (ab)  
print (ab)
print(cd(8,2))      # here most recent module(module2) will execute'''

        # ------type(6) with classes

'''import module1
from module2 import department, university

print(department().IT())
print(module1.house().beaconites())

b = module1.house().beaconites()        # now all path save in 'b', b = beaconites()
print(b)    '''

        # ---------type(7)

'''from module2 import university, department
from module1 import university

print(university().UOS())       # most recent class obj calls '''