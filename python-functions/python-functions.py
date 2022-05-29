
# Built In Function len
string = 'abcde'
print(f'Length of the string "{string}":' , len(string))

# Creating a User Defined Function
def function_name(argument1 = 'default argument 1' , argument2 = 'default argument 2'):
    '''This is function doc string''' 

    print('These are the passed arguments :' , (argument1 , argument2))

# Calling function
function_name()

# Printing docstring
print(function_name.__doc__)

# Taking Multiple Args
def function(*args , **kwargs):
    print('These are the passed arguments :' , args)
    print('These are the passed key word arguments :' , kwargs)

# args in function is taken as a tuple and kwargs is taken as a dictionary
function(1 , 2 , 3 , 'abc' , key1 = '123' , key2 = '456' , key3 = '789')

##############################################################################################


# Return a value in function
# 3 is default value here if no value is passed
def function_that_return(value = 3):
    # Multiply value by 2 and return that number
    return value * 2

# Function that has no code but still not give error
def function_that_pass():
    pass

print(function_that_return(5))
function_that_pass()

##############################################################################################