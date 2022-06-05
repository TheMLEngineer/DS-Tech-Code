

# Single Inheritance
# Parent Class
class A:
    def place(self):
        print('Method output of A Class')

#Child Class
class B(A):
    def __init__(self):
        print('Currently in B Class')

b_object = B()
b_object.place()

##############################################################################################

# Multiple Inheritance
# First Base Class
class A:
    def greet(self):
        print('Method output of A Class')

# Second Base Class
class B:
    def greet(self):
        print('Method output of B Class')

# Child Class
class C(A , B):
    pass

# Here Method output of A Class is printed due to Method Resolution Order in Python
c_object = C()
c_object.greet()


##############################################################################################

# Multi Level Inheritance
# Base Class
class A:
    class_a_variable = 1
    def greet(self):
        print('Method output of A Class')

class B(A):
    class_b_variable = 3
    def greet(self):
        print('Method output of B Class')

# Class C will have access to both class A and class B attributes and methods
class C(B):
    print('Class A Variable :' , A.class_a_variable)
    print('Class B Variable :' , B.class_b_variable)



##############################################################################################

# Composition
class A:
    def __init__(self):
        print('Class A Object Created')
    def greet(self , name):
        print(f'Hello {name}')

class B:
    
    # Here we create class A object
    class_a_object = A()
    # Here we can reuse class A method in class B , Achieving code reusability without inheritance
    class_a_object.greet('')


##############################################################################################