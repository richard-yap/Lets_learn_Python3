#---------------------------------MODULE 3---------------------------------
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

#-----------Arithmetic operators----------
print(2*3)#multiplication operator
print(2**3)#power operator
print(8/3)#division operator
print(8//3)#floor division getting the integer
print(8%2)#modulo operator gives you the remainder of the division

#----------------------------compound operators----------------------------
a = 2
a += 1
a = a + 1

#---------------------------comparison operators----------------------------
a = 100
b = 5
c = -5
d = 5

print(a > b)
print(b < c)
print(b >= c)
print(c <= b)
print(a == b + d)
print(d <= a + c)
print(c != b)

#-------------------------membership operators----------------------------
listc = [1, 2, 7, 8]
1 in listc

bool('')
bool(' ')

'123' == '123' #this is better to check equality
'123' is '123' #checks whether they are the same memory address

#-----------------------------logical operators------------------------------
# iterates thr list of boolean to give one boolean
all([True, True, False])

# any() function gives "or"
any([False, True])
