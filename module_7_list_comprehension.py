#--------------------------LIST COMPREHENSION-------------------------------
# syntatic sugar
# python advanced shortcuts
# unique in python

[n ** 2 for n in range(10)]

#map method
list(map( lambda x : x ** 2, range(10)))

#map + filtering
# the filter will be done on the data before the map
[n ** 2 for n in range(10) if not n % 2]

#exercise
[n ** 2 for n in range(1, 100) if not n % 3 and not n % 5][:20]

#teacher's answers:
is_divisible = lambda x, y : x % y == 0
list_1 = [n ** 2 for n in range(100) if not is_divisible(n, 3) and not is_divisible(n, 5)][:20]

#exercise 2
ex = "Today is a great day"
[w[0] for w in ex.split()]

# or
words = ex.split()
get_first_letter = lambda x: x[0]
[get_first_letter(x) for x in words]

#------------------------------SET COMPREHENSION------------------------------
# same thing as how you'd write a list comprehension but in curly brackets {}
{get_first_letter(x) for x in words}

#------------------------------DICT COMPREHENSION------------------------------
{i : i*i for i in range(1, 11) if i % 2 == 0}

#----------------------------------GENERATOR-----------------------------------
# generator is like a ticket machine
# only if you want to have a more efficient method to compute yr result
# since it takes up less RAM space

# two types
# generator expression is also known as a comprehension but in the form of a tuples
# generator
#using the list() function will cause the memory to pull out all the numbers

#gives a generator because python is using generator
mygen = (n * n for n in range(10))

# only one number is pulled out at one time
#compared to for loops for loops is like an automated ticketing machine, will keep calling next
next(mygen)

# using the loop method
#however you can only loop one time
for i in mygen:
    print(i)

#exercise
namelist = ["ally", "jane", "berlinda"]
name_gen = (i.capitalize() for i in namelist)
next(name_gen)

#--------------------------------GENERATOR FUNCTION----------------------------------
# for generator loops you have to use yield, not return
#  if your logic is more compliacated
def even(n):
    for i in range(n):
        if i % 2 == 0 : yield i:

test = even(10)
next(test)
