# A Simple Decorator
def actual_function(func):
    def inside_wrapper_function():
        print("Blah Blah Blah before the function is called.")
        func()
        print("Blah Blah after the function is called.")
    return inside_wrapper_function
def hello():
    print('Hello')

say_hello = actual_function(hello)
print(say_hello())


##############################################################################################

# A Simple Decorator using @
def actual_function(func):
    def inside_wrapper_function():
        print("Blah Blah Blah before the function is called.")
        func()
        print("Blah Blah Blah after the function is called.")
    return inside_wrapper_function
@actual_function
def say_hello():
    print('Hello')
print(say_hello())

##############################################################################################


# Using some random name as a decorator
@random_function_name
def say_hi():
    print('Hi')


##############################################################################################

# Using two decorators on one function

def blah(func):
    def inside_wrapper_function():
        print("Blah Blah Blah before the function is called.")
        func()
        print("Blah Blah Blah after the function is called.")
    return inside_wrapper_function
def semi_colon(func):
    def inside_wrapper_function_1():
        print(";) ;) ;) before the function is called.")
        func()
        print(";) ;) ;) after the function is called.")
    return inside_wrapper_function_1
@blah
@semi_colon
def say_hello():
    print('Hello')
print(say_hello())


##############################################################################################
