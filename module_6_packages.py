#-------------------------------MODULE 6---------------------------------
#a package is a folder of python file
#a module is a python file

#------------------------installing packages----------------------------
pip install {package}
pip install numpy
pip install matplotlib

#--------------------------some modules-------------------------------
import time
print('hello')
time.sleep(3)
print('world')

import random

#system module that lets you get the args from a python execution
import sys

#if you want to scrape data!!**
import urllib.request
#example:
with urllib.request.urlopen("http://python.org/"):
    html = f.read()
print(html)

#importing everything
import math as m
import math
from math import *

# importing selectively
from math import sin, pi

#---------------------------creating a package??------------------------------



#--------------------------PRACTICE_1----------------------------
numbers_divisibleby7_notmultipleof5 = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        numbers_divisibleby7_notmultipleof5.append(i)
print(numbers_divisibleby7_notmultipleof5)

# method 2
list(filter(lambda num : (num % 7 == 0 and num % 5 != 0), range(2000, 3201)))

#---------------------------PRACTICE 2-----------------------------------

bank_amount = 0
while (True):
    keyword = input("what is your transaction log")
    #guard clause
    if (keyword == "exit"):
        bank_amount = 500
        print(bank_amount)
        break
    #the program
    input_list = keyword.split()
    input_amount = float(input_list[1])
    if input_list[0] == "D":
        bank_amount += input_amount
    if input_list[0] == "W":
        bank_amount -= input_amount
    print("Your bank balance is: ", bank_amount)

# Teacher's answers:
      

{
    "D": "300",
    "D": "300",
    "W": "200",
    "D": "100",
    "exit": "500"
}.get("C", "IDK YOUR GRADE")
