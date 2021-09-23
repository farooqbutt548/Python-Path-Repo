                    # -----List 
# List basic 

'''list_data = [1,2,3,4,5,'faroooq', 'butt', 'zaheer','irshad', 2.33,55.9]
print(list_data[4])    # 5th position 
print(list_data[ : 4])   # first 5 
print(list_data[:7:2])   # among first 8 with 2 step
list_data[2]='three'       # change 3rd index value (mutable)
print(list_data)
print(type(list_data))'''
# list add values 
'''name = [ 'farooq', 'zaheer', 'touseef']
degree = ['BS-IT', 'BS-SE', 'BS-CS']
name.append('butt')   # add at last index
print(name)
name.insert(1, 'engineer')  # add at desired index (i like this method not append)
print(name)
print(name+degree)      # concatination two lists
name.extend(degree)  # joined both lists, name & degree
print(name)     # now name has all values'''
# list remove data 
'''uni = ['UOS', 'NUST', 'MY-UNI', 'NUT', 'UOS','LUMS', 'NFC', 'UET', 'UOJ']
print(uni.pop())  # last element poped 'UOJ'
print(uni)   # UOJ is popped
del (uni[2])
print(uni)   # 3rd my-uni is deleted
uni.remove('NFC')  # remove via name if available
print(uni)'''
# other methods in list 
'''print(uni.count('UOS'))         # count the element in list
nums =[2 ,3 ,8.44 , 6 ,5.32 , 8 ,1 ,4 ]
nums.sort()          # sorted by numbers
print(nums)
new_copy_list = nums.copy()         # copy all daya and past in new list
alphabits = ['b','d','g','s','e','c','a','f']
print(sorted(alphabits))   # sorted for this line not change list value
alphabits.sort()           # sorts alphabitically 
print(alphabits)
alphabits.clear()
print(alphabits)            # clear all data '''
# == , is difference in list
'''name1 = ['python', 'java','kotlin', 'ruby', 'c++']
name2 = ['python', 'java','kotlin', 'ruby', 'c++']
print(name1 == name2)   # values are equal  (True)
print(name1 is name2)   # values are same but not same memory location (False)'''
# convertion of lists to string and to list
'''name = input('enter your name :').split()  # string to list
print(name)         # will make list seperated by spaces
name1, name2, name3 = 'farooq butt kashmiri'.split()
print(name1, name2, name3)
# list to string 
cities = ['faisalabad ' ,'lahore ', 'islamabad ', 'rawalpindi ']
print(','.join(cities))        # convert list to string '''
# Loops in list 
'''laptops = ['dell', 'hp','lenavo', 'apple mac', 'l.g']
for i in laptops:
    print(i)'''
# nested loop in list
'''datam = [['a','b', 'c'],['d','e', 'f'],['g', 'h','i']]
for data in datam:
    for i in data:
        print(i)
print(datam[1][1])   # indext 2 of 2nd element (e)'''
 # to make list first 15 naturel nums
'''make_list =list(range(1,16))
print(make_list)'''