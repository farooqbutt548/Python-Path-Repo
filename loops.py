                                # ---Loops

#  we can get output of while_loop with for_loop and vise versa

                        # -- while_loops
'''num = int(input('enter a n_num to their sum : '))
total = 0
i = 0
while i <= num:
    total += i
    i += 1
print(f"the total sum is : {total}") '''

# while_loop with slicing      1234 = 1+2+3+4
'''number = input('enter numbers : ')
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)'''
# name letter count with while loof
'''name = input('enter your name : ')
temp_cell = ''
i = 0
while i < len(name):
    if name[i] not in temp_cell:
        temp_cell += name[i]
        print(f'the char {name[i]} is {name.count(name[i])} times in {name}')
    i +=1'''
                # ---for_loop

# sum via slicing
'''total = 0
number = input('plz enter a num to addition : ')
for i in range(0, len(number)):
    total += int(number[i])
print(total)'''
# sum of n_num with For_loop
'''num = int(input('plz enter a n_num to addition : '))
total = 0
for i in range(0,num+1):
    total+= i
print(total)'''
# letter_count with for loop
'''name = input('enter name to letter count : ')
cell = ''
for i in range(len(name)):
    if name[i] not in cell:
        cell += name[i]
        print(f'the "{name[i]}" in "{name} : {name.count(name[i])}" timkes.')'''
        # Exercise if with In-keyword
'''name = input('enter some text : ')
letter = input('enter desired letter : ')
if letter in name:
    print(f"Yup! your letter '{letter}' is present in '{name}' ")
else:
    print(f"Nop! your letter '{letter}' is not present in '{name}' ")'''