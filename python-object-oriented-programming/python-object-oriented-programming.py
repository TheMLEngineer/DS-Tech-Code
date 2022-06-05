# OOP

# Data Abstraction (Having Class / function in other .py files and importing them here to reduce coding complexity)
# Importing Greet class from abstract.py in same folder
from abstract import Greet

# Class
class Person:

    # Class Variable
    name = 'Karthik'

    # Encapsulation
    # Protected Member (Accessible within classes and subclasses)
    _age = 25
    # Private Member (Accessible only within class)
    __salary = 1200000
    
    # Method
    def print_name(self):
        print(' Name in Person Object :' , Person.name)

    # Method overloading (Compile time polymorphism)
    def function_name(self , value):
        value_dtype = type(value)
        print(f'Length of {value_dtype} : ' , len(value))


# Inheritance 
class Employee(Person):
    
    # Method overridding (Run time polymorphism)
    def print_name(self):
        print(' Name in Employee Object :' , Person.name)


# Implementing Data Abstraction and Multiple Inheritance
class Welcome(Employee , Greet):

    def welcoming(self):
        Greet.greet(self , Employee.name)

# Object
person_object = Person()
# Calling print_name() method
person_object.print_name()

# Polymorphism
person_object.function_name('String')
person_object.function_name([1 , 2 , 3])

# Inherited object
employee_object = Employee()

# Calling print_name() method on Employee object
employee_object.print_name()

# Data abstraction implementation
greet_object = Welcome()
greet_object.welcoming()

##############################################################################################