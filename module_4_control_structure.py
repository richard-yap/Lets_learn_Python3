#---------------------------------MODULE 4---------------------------------
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .

#-------------------------------CONDITIONALS--------------------------------
XiaXue_views = 126311
Roy_views = 819
BrowieTv_views = 51101

def calculator(views):
    if views >= 50000:
        print("The influencer qualifies for a payment")
        if views <= 100000:
            payment = 0.01 * views
            print("The influencer receives $", payment)
        elif views > 100000:
            payment = 0.05 * views
            print("The influencer receives $", payment)
    else:
        print("The influencer does not qualify for a payment")

calculator(XiaXue_views)
calculator(Roy_views)
calculator(BrowieTv_views)

#--------------------ANOTHER SYNTATIC SUGAR!!-------------------------
order_total = 200
discount = 25 if order_total > 100 else 0
discount
#but you cannot use elif, can only use if and else
#like this:
discount = 25 if order_total > 200 else 5 if order_total < 300 else 0
discount

#--------------------------------PRACTICE 5----------------------------------
#the input function: grades becomes the value of whatever you type
# run this code first:
grade = input("What is your grade:")

if grade == "A":
    print("Excellent")
elif grade == "B":
    print("Well done!")
# elif grade == "C" or grade == "D":
elif grade in ["C", "D"]:
    print("Work harder")
else:
    print("Idk your grade")

# or
{
    "A": "Excellent",
    "B": "Well done",
    "C": "Work harder",
    "D": "Work even harder"
}.get("C", "IDK YOUR GRADE")

#python does not have switch

#---------------------------------------------------------------------------
#-----------------while loop----------------
i = 1
while i < 10:
    print(i)
    i += 1

#------------------------------PRACTICE 6---------------------------------
fibonacci = [1, 1]
index = 0
index1 = index + 1
while fibonacci <= 100:
    new_number = fibonacci[index] + fibonacci[index1]
    index += 1
    index1 += 1
    fibonacci.append(new_number)
print(fibonacci)

#---------------------------------ANSWERS-----------------------------------
a, b = 0, 1
while (b < 100):
    print(b)
    a, b = b, a + b

#or if you want to find out what is the value of a specific fibonacci number
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum
fib(10)
#--------------------------------FOR LOOPS---------------------------------
#--------range() function--------------------
# range(start, stop, step)
list(range(0, 101, 2)) #even numbers

list(range(1, 101))

#--------------------------------PRACTICE 7-------------------------------
squares = []
for i in list(range(1, 11)):
    i = i**2
    squares.append(i)
print(squares)

#-------------------------------------------------------------------------
#------Enumerate----
heights = [170,160,155]
persons = ["Alfred", "Ally", "Berlinda"]

#if you don't put list, you won't get the result
list_of_persons_tuple = list(enumerate(persons))
print(list_of_persons_tuple)

for i, person in enumerate(persons):
    height = heights[i]
    print("h: {}\nname: {}".format(height, person))

#returns list of tuples
list(zip(persons, heights))

#--------------------------PRACTICE 8------------------------------------
names = ["Ally", "Berlinda", "Jane"]
heights = [170,159,161]
weights = [60,55,45]

list(zip(names,heights,weights))

for name, height, weight in zip(names,heights,weights):
    print("h: {}\nname: {}\nweight: {}".format(name, height, weight))

#-----------------------------------BREAK--------------------------------
for x in range(1, 5):
    if(x == 3): break
    print(x)
#----------------------------------CONTINUE---------------------------------
for x in range(1, 5):
    if(x == 3): continue
    print(x)

#----------------------------PRACTICE_9------------------------------
primes = []
for n in range(1, 101):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)

# ctr, shift, p to see settings
