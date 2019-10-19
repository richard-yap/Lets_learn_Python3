# ---------------------MODULE 2 Data Types----------------------
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

# number/ int, float
# string
# list
# tuple
# dictionary
# set

# you can also write a variable like this in atom, but not in jupyter notebook:
a, b = 1, 2
c = a + b
a
b

# .format nicely puts them into the pcurly brackets
#.format only works with curly brackets {}
# new indexing method, the values in () function like a list
print("{} + {} = {}".format(a, b ,c))

# for hydrogen you don't have to write print all the time will return with a quotation mark
#to change the positions of a, b, c:
"{1} + {0} = {2}".format(a, b, c)

#to change the number of decimal places:
"{:.1f} + {:.2f} = {:.5f}".format(a, b, c)

#to specify how many spaces you want the character/value to occupy:
# but unable to put them in the middle
"{0:5.1f} + {1:5.2f} = {2:5.5f}".format(a, b, c)

#-----------------------------PRACTICE 1----------------------------------
a = 4.444
b = 5.555
c= 6.666
d = a + b + c

print("{1:.2f} + {2:.2f} + {0:.1f} = {3:.0f}".format(a, b, c, d))

#-------------------------------------------------------------------------
# string concatenation adding the string

"-" * 50
a = 'hello '
b = 'world!'

c = a + b

# apparantly you can multiply strings here, not sure if can in jupyter notebook though
c

#functions for variables that are strings
#but the result is a derivative, unless you link it to a variable
c.upper()
c.lower()
c.capitalize()

# replaces the string with a new string specified after the comma
c.replace("world", "Richard")


# -------------------------PRACTICE 2-----------------------------------
country = "france"
capital = "paris"

print("The capital of {} is {}".format(country.upper(), capital.capitalize()))

# -----------------------------------------------------------------------
# \n  gives new line
# \t  gives new tab

#.strip() gets rid of all the white spaces

print("\n\t Hello              ".strip())
print("             g ha wi    ".strip())

#.split() function splits the strings into a list
a = 'Today is a sunny day'
a.split()

b = 'The answer = 5'
c = b.split(' = ')
# the '' you specify becomes the spliting point
print(c)

#joining list if strings
d = ['hello', 'world', '1234']
",".join(d)

#--------------------------------PRACTICE 3----------------------------------
practice_3 = "abc@def.com"
list1 = practice_3.split("@")
print(list1[0], "is from", list1[1] )

# doing it the .format way
"{} is from {}".format(list1[0], list1[1])

# doing it the .join() way
" is from ".join(list1)

# the * unpacks the list into individual variables
# syntactic sugar :))
"{} is from {}".format(*list1)

# may be gone in python 4, but used in python2 when .format was not available, seen in javascript and c
f"{list1[0]} is from {list1[1]}"

#---------------------------------------------------------------------------
# .find() function
a = 'Today is a nice day'
a.find('nice')
a.find('z')

# .count() function
b = "aiwnecouebeo"
b.count('b')

#--------------------------------LISTS-------------------------------------
# the [] notation also applies to a string
# you can think of strings as an ordered collection

b = 'hello2'
b[0]

lista = [7, 8, 9, 10, 11]

# cloning the list:
new_list = lista[:]
print(new_list)
lista[1:]
lista[::-1]
lista[:2]

#cloning list method 2
v = lista.copy()
print(v)

# finding number of items in the list/ string
len(lista)
len(b)

# to obtain the index position in the list:
lista = [7, 8, 9, 10, 11]
lista.index(9)

#mutative/transformative/mutable functions
#extending the list:
lista.append(10)
print(lista)

#specific location:
# lista.insert(position, value)
lista.insert(2, 99)
print(lista)

#deleting
#don't use del lista[2] <- may be removed in python 4
# use with parenthesis
del(lista[2])
print(lista)

#getting back the value
lista.pop(2)

#---------------------------------------------------------------------------
#mutative sort
listb = [3, 6, 1, 0, 5]
listb.sort()
listb

#derivative sort
sorted(listb)

#reverse the list
listb.reverse()
listb

listb[::-1]

#---------------------------PRACTICE 4----------------------------------
letters = list("ACCATTGACA")
letters
# 1.
letters.count("A")
# 2.
letters.index("T")

# 3.
letters2 = letters[:]
letters2.remove("G")

# 4.
letters2
letters2.insert(2, "A")
letters2

# 5.
reverse_letters2 = letters2[::-1]
print(reverse_letters2)

#----------------------------------TUPLES---------------------------------
# if you don't put parenthesis, it will become a TUPLE
a = 1, 2, 3, 4, 5
a

n,m = 3,4
n
m

#----------------------------------DICTIONARIES-------------------------------
# the keys you use must be immutable (tuple, strings or numbers)
new_dict = {}
new_dict[(1,4)] = 'happy'
new_dict
# dictionary are not ordered

# You can also insert an item to a dictionary by using the update() method, e.g.:

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

dict.update({"duck" : "canard"})
print(dict)

# To remove the last item in a dictionary, you can use the popitem() method:

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

dict.popitem()
print(dict)    # outputs: {'cat' : 'chat', 'dog' : 'chien'}

# This is done with the del instruction.
#
# Here's the example:

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

del dict['dog']
print(dict)
#------------------------------------SETS--------------------------------------
s = {1,2,3,1,2,3}
s
#the set will take out duplicates, values will be unique

#--------------------------------PRACTICE 4-----------------------------------
sent = "Peter reads a book on a table"
list_sent = sent.split()
set_sent = set(list_sent)
print(list_sent)
print(set_sent)
len(set_sent)

#-----------------------------------------------------------------------------
