                                              # ---- Dictionary

'''designation = {'farooq':'c.e.o', 'zaheer':'cfo', 'waqas': 'accountant'}     # dictionary (key:value)
print(designation)
print (type(designation))
marks = dict (ict = 97, dld= 88, algebra = 87, ai = 55)     # dict method is used (i like this method)
print(marks)
print(type(marks))

print(designation['zaheer'])
# simple dictionary
bio = dict(name = 'farooq',
 age= 25,
  degree = 'BS-IT',
   roll_num = 660,
    City = 'Faisalabad',
     Phon = 923015902110)
print(bio['degree'])
                    # dictionary in dictionary
phon_num = dict(
    farooq = dict(jazz = 923015902110, zong = 923179600604),
    afzal = dict(jazz =  923004049286, zong = 923184049286),
    zaheer = 923007663624
)
print(phon_num)
print(phon_num['farooq']['zong'])       # access dictionary in dictionary value

                    # Add in Dictionary 
empty = {}
empty['sargodha'] = 'UOS'
empty['lahore'] = 'UET'
empty['islamabad'] = 'AIOU'
empty['faisalabad'] = 'GCUF'
print(empty)
del empty['faisalabad']     # delete the (key :value)
print(empty)

alphabet = dict(a='b', c='d', e='f')
alphabet.clear()           # will delete all entire entries
print(alphabet)

city = input('input city : ')
if city in empty:                           # for finding key. for integer we will make it int form
    print('Yup! here in dictionary.')       
else:
    print('Nope! not in dictionary.')

uni = input('input uni : ')
if uni in empty.values():                           # for finding value 
    print('Yup! here in dictionary.')       
else:
    print('Nope! not in dictionary.')

empty = {}
empty['sargodha'] = 'UOS'
empty['lahore'] = 'UET'
empty['islamabad'] = 'AIOU'
empty['faisalabad'] = 'GCUF'
print(empty.values())               # -------- all values will print
for i in empty.values():    
    print(i)                        # -------- all values will print

for i in empty.keys():                     # -------- all keys will print.... (either use key method or not)
    print (i)

                                        # ---------- items method
empty = {}
empty['sargodha'] = 'UOS'
empty['lahore'] = 'UET'
empty['islamabad'] = 'AIOU'
empty['faisalabad'] = 'GCUF'
item_method = empty.items()         # make a list of tuples of key, values
print(item_method)
print(type(item_method))
# Example of item method
for city, uni in empty.items():
    print(f'the {city} has {uni} populer university')      # looping with item method

new_empty = empty.pop('faisalabad')         # popped item stored in new_empty
print(new_empty)
print(type(new_empty))
print(empty)                    # faisalabad is popped 

news_empty = empty.popitem()    # randomply pop and save in variable
print(news_empty)
print(type(news_empty))
                                    # -------- update method
student = dict(name = 'farooq', 
                    caste = 'kashmiri',
                    roll_num = 660,
                    uni = 'UOS',
                    degree = 'BSIT')

more_info = dict( home_town = 'faisalabad',
                    adress = 'orchards home',
                    name = 'Muhammad Farooq',
                    cell_num = 923015902110)
print(student)
print(more_info)
student.update(more_info)
print(student)                  # merge both info and 'name' will update as of more_info
student.update({})
print(student)                  # nothing will update same previos information
            # ------- get method
print(more_info.get('adress'))          # value of adress
print(more_info.get('adresses'))        # give 'none' not error
# copy method 

a = dict(name = 'farooq', caste = 'butt', age = 25)
b= a.copy()             # two same but different dictionary , a! = B
a.pop('age')
print(a)
print(b)

# EXERCISE No. 1     (key, key*3)
def cube_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes
print(cube_finder(10))

# EXERCISE No. 2    (key, key*2) 
def twice(n):
    twice_dict = {}
    for i in range(1,n+1):
        twice_dict[i] = i*2
    return(twice_dict)

print(twice(10)) 
# EXERCISE No. 3
def info (data):
    info_dict = {}
    a = input('enter name : ')
    b = input('enter age :')
    c = input('enter degree :')
    d = input('enter uni :')
    e = input('enter number :')
    info_dict['name'] = a
    info_dict['age'] = b
    info_dict['degree'] = c
    info_dict['uni'] = d
    info_dict['number'] = e
    return(info_dict)

data = {}
print(info(data).items())  '''