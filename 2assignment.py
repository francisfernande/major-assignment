#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Explain what inheritance is in object-oriented programming and why it is used.
A1. Inheritance in object-oriented programming (OOP) is a mechanism that allows one class (called the derived or subclass) to 
    inherit properties and behaviors (i.e., attributes and methods) from another class (called the base or parent class).
    It is used to create a hierarchy of classes where the derived class can reuse and extend the functionality of the base class.
    Inheritance promotes code reuse and helps in organizing and structuring code.


# In[ ]:


2. Discuss the concept of single inheritance and multiple inheritance, highlighting their
differences and advantages.
A2.Single Inheritance and Multiple Inheritance:

Single Inheritance: In single inheritance, a derived class inherits from only one base class. 
This is a simpler form of inheritance and is less prone to ambiguity and conflicts.

Multiple Inheritance: In multiple inheritance, a derived class can inherit from more than one base class. 
This allows for combining features from multiple sources, but it can lead to ambiguity and conflicts when two base classes 
have methods or attributes with the same name. 

Advantages:

Single Inheritance is simpler and easier to understand.
Multiple Inheritance can provide greater flexibility by combining features from multiple sources.



# In[ ]:


3. Explain the terms "base class" and "derived class" in the context of inheritance.
A3. Base Class and Derived Class:

Base Class: Also known as the parent class or superclass, it's the class from which other classes inherit attributes and methods.

Derived Class: Also known as the child class or subclass, it's the class that inherits properties and behaviors from the base class 
and can also add its own unique attributes and methods.


# In[ ]:


4. What is the significance of the "protected" access modifier in inheritance? How does
get_ipython().run_line_magic('pinfo', 'modifiers')
A4. The "protected" access modifier in inheritance:

class Parent:
    def __init__(self):
        self._protected_var = 10  # A protected variable
        
"protected" members (attributes and methods) are accessible within the class itself and within its derived classes.
It differs from "private" members, which are only accessible within the class that defines them.
It differs from "public" members, which are accessible from anywhere.


# In[ ]:


5. What is the purpose of the "super" keyword in inheritance? Provide an example.
A5. The "super" keyword in inheritance is used to call a method from the parent class (base class) within the context of the 
child class (derived class). It's often used when a method in the derived class overrides a method in the base class, and you 
want to invoke the base class's method as well.


# In[1]:


class Parent:
    def show(self):
        print("This is the parent class.")

class Child(Parent):
    def show(self):
        super().show()  # Calling the parent class's show method
        print("This is the child class.")

c = Child()
c.show()


# In[ ]:


6. Create a base class called "Vehicle" with attributes like "make", "model", and "year".
Then, create a derived class called "Car" that inherits from "Vehicle" and adds an
attribute called "fuel_type". Implement appropriate methods in both classes.


# In[2]:


#A6.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type


# In[ ]:


7. Create a base class called "Employee" with attributes like "name" and "salary."
Derive two classes, "Manager" and "Developer," from "Employee." Add an additional
attribute called "department" for the "Manager" class and "programming_language"
for the "Developer" class.


# In[3]:


#A7.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


# In[ ]:


8. Design a base class called "Shape" with attributes like "colour" and "border_width."
Create derived classes, "Rectangle" and "Circle," that inherit from "Shape" and add
specific attributes like "length" and "width" for the "Rectangle" class and "radius" for
the "Circle" class.


# In[6]:


#A8.
class Shape:
    def __init__(self, colour, border_width):
        self.colour = colour
        self.border_width = border_width

class Rectangle(Shape):
    def __init__(self, colour, border_width, length, width):
        super().__init__(colour, border_width)
        self.length = length
        self.width = width

class Circle(Shape):
    def __init__(self, colour, border_width, radius):
        super().__init__(colour, border_width)
        self.radius = radius


# In[ ]:


9. Create a base class called "Device" with attributes like "brand" and "model." Derive
two classes, "Phone" and "Tablet," from "Device." Add specific attributes like
"screen_size" for the "Phone" class and "battery_capacity" for the "Tablet" class.


# In[7]:


#A9.
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Phone(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

class Tablet(Device):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity


# In[ ]:


10. Create a base class called "BankAccount" with attributes like "account_number" and
"balance." Derive two classes, "SavingsAccount" and "CheckingAccount," from
"BankAccount." Add specific methods like "calculate_interest" for the
"SavingsAccount" class and "deduct_fees" for the "CheckingAccount" class.


# In[ ]:


#A10.
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def calculate_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deduct_fees(self, fee):
        self.balance -= fee

