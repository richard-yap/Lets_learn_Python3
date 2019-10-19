#-------------------------------MODULE 5--------------------------------------
#-----------------------Functions--------------------------

#-----------------------------PRACTICE_10-----------------------------------
BOOKING_FEE = 5
STARTING_PRICE = 2
RATE = 1.5

def calculate_taxifare(distance):
    taxi_fare = BOOKING_FEE + STARTING_PRICE + distance*RATE
    return(taxi_fare)

calculate_taxifare(10)

#returns a tuple and you can unpack similar to the previous one
def f(x):
    return x, 2*x

f(1)

#---------------------------PRACTICE_11----------------------------
tax = 0.07
disc_percent = 0.25
disc_threshold = 200

def calculator(order):
    disc_amt = discount*order/100
    tax = 0.07(order - disc_amt)
    if order > disc_threshold:
        discount = disc_percent
    else:
        discount = 0
    return(disc_amt, tax)

calculator(202)

#the parameter will replace the argument

#---------------------variable arguments-------------------------
def my_sum(a, *c):
    s = a
    for i in c:
        s += i
    return s

# *c is a tuple, so is this case c is (1, 1, 1)
my_sum(1, 1, 1, 1)


# must be in this order:
# 1. required args f(a, b, d)
# 2. default args e.g f(d = 5, a = 1)
# 3. variable args f(*a, *b, *f)

#-----------------------------PRACTICE_12-----------------------------------
def my_min(a, *turple_of_numbers):
    for i in turple_of_numbers:
        if i < a:
            a = i
    return(a)
my_min(1, 1212, 9, -1)

#------------------------------------------------------------------
#another way to define a function:
square = lambda x : x*x

#method 1
def f1(x, y):
    return(10*(x + y))
#vs method 2
f2 = lambda x, y : 10*(x + y)

f1(1, 2)
f2(1, 2)
#-----------------------Applications of lambda------------------------
#--------------------------------MAP----------------------------------
#map() function helps you do mathematical operations on the list or lists
# if too complicated can fall back to for loops
#you can think lambda as convert something to something

a = [1, 2, 3]
# the argument is the lambda, then pass on the list
list(map(lambda x: x*x, a))

#practice_13
#using multiple lists
x = [0, 1, 2, 3]
y = [2, 4, 6, 8]
practice_13 = lambda x, y : 10*x + y
list(map(practice_13, x, y))

#practice 13 but loop method:
c = []
for a,b in zip(x,y):
    c.append(10*a+b)
print(c)

#-------------------------------FILTER----------------------------------
#think filter as getting rid of everthing except the one you want
a = [2, 3, 4, 5, 6]
b = filter(lambda x: x > 3, a)
list(b)

#filter is a shortcut to writing a conditional for loop
f = lambda x: x > 1
list(filter(f, [1, 2, 3]))
