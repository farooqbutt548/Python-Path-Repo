                        # ----- Tuple 

'''tup1 = (1,2,3,4,5,6.0)
for i in tup1:              # we can use while loop too
    print(i, end=' ')

uni_tuple = (1,)          # is tuple not int
print(type(uni_tuple))
also_tuple = tuple (range(1,11))
print(type(also_tuple))

unies = 'UOS', 'NUST', 'UET', 'FAST', 'MYU', 'AIOU'
print(type(unies))          # tuples without bracess
# List in Tuple (Tuple is immutable but list in it is mutable)
list_tuple = (1,5, 'butt', ['first', 'second', 'last'])
list_tuple[3].pop()
print(list_tuple)       # 'last' will be removed
list_tuple[3].append('new last')
print(list_tuple)
print(min(tup1))
print(max(tup1))
print(tup1+tup1)'''