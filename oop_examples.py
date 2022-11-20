## OOP - Youtube tips
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def salary(self):
        return '{}'.format(self.pay)
    def companyEmail(self):
        return '{}'.format(self.email)
        
emp_1 = Employee('Brad', 'Roehrig', 150000)
emp_2 = Employee('Grace', 'Roehrig', 200000)

print(emp_1.fullname())
print(emp_1.salary())
print(emp_1.companyEmail())

print(emp_1.first, emp_1.last, emp_1.pay, emp_1.email)
print(emp_2.first, emp_2.last, emp_2.pay, emp_2.email)

emp_1.fullname()

print(Employee.fullname(emp_1))

emp_1.first = "Bud" #Changes attribute
print(Employee.fullname(emp_1))

## OOP - Banking app

class User:		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

User()
guido = User()
monty = User()
# Accessing the instance's attributes
print(guido.name)	# output: Michael
print(monty.name)	# output: Michael

guido.name = "Guido"
print(guido.name) # output: Guido
monty.name = "Monty"
print(monty.name) # output: Monty

class User:
    # declaring a class attribute
    bank_name = "First National Dojo"		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

guido = User()
monty = User()
guido.bank_name = "Dojo Credit Union"
print(guido.bank_name) # output: Dojo Credit Union 
print(monty.bank_name) # output: First National Dojo

User.bank_name = "Bank of Dojo"
print(guido.bank_name) # output: Bank of Dojo 
print(monty.bank_name) # output: Bank of Dojo

class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self, name, email_address):
    # we assign them accordingly
        self.name = name
        self.email = email_address
    	# the account balance is set to $0
        self.account_balance = 0
guido = User("Guido Van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python
print(monty.bank_name)
print(guido.bank_name)

monty.bank_name = "Dojo Credit Union"

print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python
print(monty.bank_name)
print(guido.bank_name)

## User Assignment OOP

class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


brad = User("Brad")
matt = User("Matt")
grace = User("Grace")

brad.make_deposit(300)
brad.make_deposit(200)
brad.make_deposit(500)
brad.make_withdrawl(100)
brad.display_user_balance()

matt.make_deposit(1000)
matt.make_deposit(1000)
matt.make_withdrawl(500)
matt.make_withdrawl(300)
matt.display_user_balance()

grace.make_deposit(3500)
grace.make_withdrawl(1000)
grace.make_withdrawl(500)
grace.make_withdrawl(1000)
grace.display_user_balance()


brad.transfer_money(400, grace)

## User Assignment OOP - Chaining

class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawl(self,amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self
    
    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

brad = User("Brad")
matt = User("Matt")
grace = User("Grace")

brad.make_deposit(300).make_deposit(200).make_deposit(500).make_withdrawl(100).display_user_balance()

matt.make_deposit(1000).make_deposit(1000).make_withdrawl(500).make_withdrawl(300).display_user_balance()

grace.make_deposit(3500).make_withdrawl(1000).make_withdrawl(500).make_withdrawl(1000).display_user_balance()


brad.transfer_money(400, grace)

## BankAccount Project @classmethod

class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()
        
savings = BankAccount(.0225,350000)
checking = BankAccount(.3,500000)

savings.deposit(10).deposit(20).deposit(40).withdraw(600).yield_interest().display_account_info()
checking.deposit(100).deposit(200).deposit(400).withdraw(60).yield_interest().display_account_info()

BankAccount.print_all_accounts()

## UsersWithBankAccountsProj

class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        return f"{self.balance}"

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


class User:

    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.02,1000),
            "savings" : BankAccount(.05,3000)
        }
        

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


adrien = User("Adrien")

adrien.account['checking'].deposit(100)
adrien.display_user_balance()

#Encapsulation - the idea that we can group code together into objects; hence Object Oriented Programming. We use classes or "coding blue prints" to define what our objects are and how they behave. We encapsulate attributes and methods in our class.
class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")

#Inheritance - the idea that we pass along attributes and methods from one class into a "sub-class" or child class, and not have to re-write the code to make it work.  Child classes can be more specific versions of their Parent class.  Using the key word "super" will call methods
class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super.brew_now(beans)
        print("Frothy!!!")

#Polymorphism - means "many forms", and the idea in OOP is that a Child class can have a different version of a method than the Parent class. In this example the child class of CappuccinoM has a clean method, and so does CoffeeM. Depending on the class, the clean method will do different things.
class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super.brew_now(beans)
        print("Frothy!!!")
    def clean(self):
        print("Cleaning the froth!")

#Abstraction is an extension of Encapsulation, and we can hide attributes or methods that a Barista doesn't need to know about, like a CoffeeM. That way the Barista can make a cup of coffee in a simpler manner.
class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe")
    def make_coffee(self):
        self.cafe.brew_now()

#Inheritance (SUPER)

#Child
class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)	
        self.is_roth = is_roth	

#Parent        
class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

#Inheritance (SUPER)

#Child
class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
    	    amount = amount * 1.10
        super().withdraw(amount)
        return self

#Parent        
class BankAccount:
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

## Module import

#modular_example/arithmetic.py
def add(x, y):
    return x + y
def multiply(x, y):
    return x * y
def subtract(x, y):
    return x - y

#modular_example/calculations.py
import arithmetic
print(arithmetic.add(5, 8))
print(arithmetic.subtract(10, 5))
print(arithmetic.multiply(12, 6))

#Module Import

# sample_project
#     |_____ python_file.py
#     |_____ my_modules
#                 |_____ __init__.py
#                 |_____ test_module.py
#                 |_____ another_module.py
#                 |_____ third_module.py
                

# import my_modules.test_module
# #or
# from my_modules import test_module


# modular_example/arithmetic.py







class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()
        
savings = BankAccount(.0225,350000)
checking = BankAccount(.3,500000)
roth = BankAccount(.4, 100000)

savings.deposit(10).deposit(20).deposit(40).withdraw(600).yield_interest().display_account_info()
checking.deposit(100).deposit(200).deposit(400).withdraw(60).yield_interest().display_account_info()
roth.deposit(100).deposit(200).deposit(400).withdraw(60).yield_interest().display_account_info()

BankAccount.print_all_accounts()