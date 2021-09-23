ab = "this is module1's variable"

# Addition
def add (a,b):
    return(a+b)

# Subtraction
def sub (a,b):
    return(a-b)

# Febonacci 
def febonacci (n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b)
    else:
        print(a, b, end= ' ')
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b, end=' ')

# Nth Number
def n_add (n):
    cell = 0
    for i in range(n+1):
        cell+=i
    print(cell)

def cd(a,b):
    return(a//b)

class house:
    def beaconites(name):
        return('this is beaconites tech : ')

class university:
    def UOS(name):
        return('this is new uni')
