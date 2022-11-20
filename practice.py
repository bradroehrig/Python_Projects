# ****************************************************************************
my_name = "Brad"
my_age = 47
retirement_age = 62
job = "Computer Nerd"

print ("My name is ", my_name, " and I'm ", my_age, " years ")

print (retirement_age - my_age, "years until", my_name, "can retire.")

# job = input("what is you job?")
print (my_name, "is a", job, "!")

print (f"{my_name} is a {job}!")
# ****************************************************************************
for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
# ****************************************************************************
def my_function():
    print("Hello")
    name = input("Your name:")
    print("Hello")
    
print (my_function())
# ****************************************************************************
def add(n1, n2):
    return n1 * n2

result = (add(2,3))

print (result)
# ****************************************************************************
n = 2
def my_function():
    n = 3
    print(n)
print(n) #Prints 2
print(my_function()) #Prints 3
# ****************************************************************************
def divide(n1, n2):
	result = n1 / n2
	print (result)
#Option 1:
divide(10, 5)
#Option 2:
divide(n2=10, n1=50)
# ****************************************************************************
age = int(input("What is your age?"))
if age > 20:
	print("Congrats, you can legally drink!")
else:
	print ("Sorry, you have to wait a few years.")
# ****************************************************************************
# weather = "sunny"
weather = input("How is the weather today?")
if weather == "rain":
	print("Bring umbrella!")
elif weather == "sunny":
	print("Bring sunglasses!")
elif weather == "snow":
	print ("Bring gloves!")
# ****************************************************************************
score = int(input("What is your score?"))
if score > 89:
	print("Your grade is an A!")
elif score < 90 and score > 79:
	print("Your grade is an B!")
elif score < 80 and score > 69:
	print("Your grade is an C!")
elif score < 70 and score > 59:
	print("Your grade is an D!")
elif score < 60:
	print("Your grade is an F!")
# ****************************************************************************
n = 0
while n < 100:
	n+=1
	print (n)
# ****************************************************************************
all_fruits = ["apple", "banana", "orange"]
for fruit in all_fruits:
	print(fruit)
# ****************************************************************************
for _ in range(100):
	print("Holy Cow!")
# ****************************************************************************
n = 0
while n < 100:
	n += 1
	if n % 2 == 0:
		continue
	print(n)
#Prints all the odd numbers
# ****************************************************************************
list1 = [1, 2, 3]
list2 = [9, 8, 7]
new_list = list1 + list2
print(new_list)
print(list1)
print(list2)
# ****************************************************************************
all_fruits = ["apple", "banana", "orange"]
print("Original List", all_fruits)
all_fruits.append("pear")
print("Appended List", all_fruits)
# ****************************************************************************
letters = ["a", "b", "c"]
print (letters[0]) #Result:"a"
print (letters[-1]) #Result: "c"
print (letters[1:3]) #Result: "b c"
print (letters)
# ****************************************************************************
# range(start, end, step)
for i in range(6, 0, -2):
	print(i)
# ****************************************************************************
# range(start, end, step)
for i in range(2, 100, 2):
	print("Hello", i)
# ****************************************************************************
import random
# randint(start, end)
n = random.randint(2, 5)
print (n)
#n can be 2, 3, 4 or 5.
# ****************************************************************************
number = 1.5
numb_round = round(number)
print (numb_round)
# result 2
# ****************************************************************************
number = -1.5
numb_abs = abs(number)
print (numb_abs)
# result 1.5
# ****************************************************************************
import random
n = random.randint(3, 10)
print(n)

# ****************************************************************************
#Classes and Object
class Car:
	pass #empty instance
# ****************************************************************************
class Car:
	def drive(self):
		print("move")
	def speed(self):
		print("speed")
my_honda = Car()
my_honda.drive()
my_toyota = Car()
my_toyota.speed()
# ****************************************************************************
class Car:
	colour = "black"
car1 = Car()
print(car1.colour) #black
# ****************************************************************************
class Car:
	def __init__(self):
		print("Building car")
my_toyota = Car()
#You will see "building car"#printed.
# ****************************************************************************
class Dog:
 
    # class attribute
    attr1 = "mammal"
    attr2 = "reptile" 
 
    # Instance attribute
    def __init__(self, name):
        self.name = name
 
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
 
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is a {}".format(Tommy.__class__.attr2))
 
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

# Rodger is a mammal
# Tommy is also a mammal
# My name is Rodger
# My name is Tommy
# ****************************************************************************
class Dog:
 
	# class attribute
	attr1 = "mammal"
	attr2 = "reptile" 
 
	# Instance attribute
	def __init__(self, name, age):
		self.name = name
		self.age = age
 
# Driver code
# Object instantiation
Rodger = Dog("Rodger", 47)
Tommy = Dog("Tommy", 23)
 
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is a {}".format(Tommy.__class__.attr2))
 
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("and I'm {}.".format(Rodger.age))
print("My name is {}".format(Tommy.name))
print("and I'm {}.".format(Tommy.age))
   
# Rodger is a mammal# 
# Tommy is a reptile
# My name is Rodger
# and I'm 47.
# My name is Tommy
# and I'm 23.

# ****************************************************************************
# Python code to demonstrate how parent constructors
# are called.
 
# parent class
class Person(object):
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
 
    def display(self):
        print(self.name)
        print(self.idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
     
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
 
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
 
 
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
 
# calling a function of the class Person using
# its instance
a.display()
a.details()
# ****************************************************************************








