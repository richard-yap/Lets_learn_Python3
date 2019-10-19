#------------------OBJECT ORIENTED PROGRAMMING--------------------------------
# class means blueprint
# instance of the class there is a difference

#define a class
#example:

class Animal:
    color = "Black"
    legs = 4
    def walk(self):
    # if you declare a function inside a class, you have to put self,
    #where self is referring to the instance of that class
        print("Walk")


spider = Animal()
spider.color
spider.legs

spider.walk()

#teacher example:
class Counter:
    count = 0 # the count here is the property of the class
    # init (initializer) is a special function of a class to initialize the class data or get inputs, also known as a constructor
    def __init__(self, count = 0):
        self.count = count # the count here is the property of the instance

    def increment_by_1(self):
        self.count += 1

    def increment_by_n(self, n):
        self.count += n

    def reset(self):
        self.count = 0

# there is no class Counter existing until you link it to an object
c = Counter()
c.count

c.increment_by_1()
c.count

#exercise
class Rectangle:
    def __init__(self, length, width): # also known as a constructor
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def __del__(self): # destructor i a special function which is invoked when an instance is destroyed
        print("I am being deleted")

r = Rectangle(10, 20)
r.area()
del(r)

y = Rectangle(10, 50)
y.area()
y.length = 20
y.area()

# exercise 2
class Employee:
    emp_count = 0 # emp_count is the property of the class
    def __init__(self, name, salary): # you can only do self inside the function
        self.name = name
        self.salary = salary
        Employee.emp_count += 1 # whenever an employee object is crated, emp_count increases by one

    def no_of_employees(): # the absence of self means it is a method that is part of the class
        print("Employees: {}".format(Employee.emp_count))

    def name_salary(self):
        print("Name: {}\nSalary: {}".format(self.name, self.salary))

    def __del__(self):
        Employee.emp_count -= 1 # em_count - 1 whenever object is deleted

emp = Employee("Dawn", 1000)
emp2 = Employee("Willy", 550)

emp.name_salary()
Employee.no_of_employees()
del(emp2)
Employee.no_of_employees()

#--------------------------------INHERITANCE---------------------------------
# a class can inherit properties of a parent
# but cannot inherit the things that i to the class, can only inherit the instances of the class

# teacher example
class Animal:
    def __init__(self, legs, color):
        self.legs = legs
        self.color = color
    def walk(self):
        print("Walk like an animal")

#when you create an animal you need to put super()
class Dog(Animal):
    def __init__(self, name, legs, color): #new property name, so must define here
        super().__init__(legs, color) # to call the parent version
        self.name = name

    def printing(self):
        return(self.legs)


a = Animal(4, "Black")
a.walk()

d = Dog("dog1", 4, "golden")
d.printing()
#------------------------------------------------------------------------------
#exercise 3
class Rectangle():
    def __init__(self, length, width): # also known as a constructor
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        # you can think it of this:
        # self.length = length
        # self.width = length
        # Square inherits the rectangle
        # length is passed two times
    def perimeter(self):
        return self.length * 4

s = Square(4)
s.area()
s.perimeter()

#------------------------------------------------------------------------------
#exercise 4
class Employee:
    emp_count = 0 # emp_count is the property of the class
    def __init__(self, name, salary): # you can only do self inside the function
        self.name = name
        self.salary = salary
        Employee.emp_count += 1 # whenever an employee object is crated, emp_count increases by one

    def no_of_employees(): # the absence of self means it is a method that is part of the class
        print("Employees: {}".format(Employee.emp_count))

    def display_details(self):
        print("Name: {}\nSalary: {}".format(self.name, self.salary))

    def __del__(self):
        Employee.emp_count -= 1 # em_count - 1 whenever object is deleted

#------------------------------------------------------------------------------
class FullTimeStaff(Employee):
    def __init__(self, name, salary, leave):
        super().__init__(name, salary)
        self.leave = leave

    def display_details(self):
        super().display_details() # no need to put self within the parenthesis because it will be inherited automatically
        print("Leave: {}".format(self.leave))

class PartTimeStaff(Employee):
    def __init__(self, name, hourly_rate):
        super().__init__(name, None) # bad design because using None means you sldn't inherit from employee
        self.hourly_rate = hourly_rate
        Employee.emp_count -= 1 # have to remove by 1 because emp_count only counts fulltimestaff not parttimestaff
        # reversal of the increment inherited from the parent Employee

    def display_details(self):
        print("Name: {}\nHourly_Rate: {}".format(self.name, self.hourly_rate))
        #don't have to put super because we are doing it differently

    def __del__(self):
        pass #do nothing instead because partimestaff are not counted in Employees

Full_timer_1 = FullTimeStaff("Harry", 4000, 10)
Part_timer_1 = PartTimeStaff("Jayce", "$8")

Full_timer_1.display_details()
