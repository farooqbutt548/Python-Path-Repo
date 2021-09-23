                                                #  Strings

# Simple String
'''string1 = ' this is 1st string,  '
string2 = "this is 2nd string"
print(type(string1))
connect_string = string1+ " "+string2
print(connect_string)
# print("errer"+3)  erreor
print('this is not error'+' ' + str(3))
print('this will print 3 times'*3 )'''
# f-string, string-formatting
'''f_name = 'farooq'
l_name = 'butt'
print(f'hello {f_name} {l_name} how are you.')
# string input via split method()
name, age,degree = input('enter your name, age & degree comma separated : ').split(',')
print(f'hello {name} your age is {age} & degree is {degree}.')
# string indexing 
name_index = 'farooq butt'
print(name_index[1])  #2nd number char will print from left
print(name_index[-1]) #last char will print
print(name_index[2:6:1])   #  string slicing [start:ending:step]
print(name_index[ : :-1])  #    reverse string'''

# string exercice 
#  name in reversed order 
'''name = input('enter your naem : ') ; print(name[::-1])'''
#  string methods
'''word = 'abCdefgHijKlmnOpqRsTuvwXyz'
print(len(word))    # leangth of word
print(word.lower())  # for lower letters
print(word.upper())  # for upper letters
print(word.count('b'))  # for count a letter in word
print(word.title())  # for first letter capital
print(word.center(80)) # for aligning text '''
