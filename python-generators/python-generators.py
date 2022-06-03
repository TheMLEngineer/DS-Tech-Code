

# range() is an Built in and frequently used generator
range_object = range(0 , 5)
print('range_object :' , range_object)
print('list of range_object ' , list(range_object))
print('*' * 50)

##############################################################################################

# Custom Generators
def generator_function(list_variable):
    for element in list_variable:
        yield element

iterator_object_created_by_generator_function = generator_function([1,2,3])
print('iterator_object_created_by_generator_function :' , iterator_object_created_by_generator_function)
for value in iterator_object_created_by_generator_function:
    print(value)
print('*' * 50)


##############################################################################################

# Function with return and yield
def function():
    yield 1
    yield 2
    yield 3
    return 5
print('Printing function() object : ' , function())
# Even though function() has return keyword , Once it has yield keyword it is treated as a generator
print('*' * 50)


##############################################################################################

def function_1():
    return 3
    print('abc')
# Here abc will not be printed as once return is used in function , function execution stops.
print('Using return : ' , function_1())

def function_2():
    yield 3
    print('abc')

# This code will print abc as even though it yields 3 , it does not stop function execution 
# so the rest of code other than other yield will run when used with list() , But when using next() only
# whatever value is yielded that is returned not the other code logic like print() 
a = list(function_2())
print('Using yield : ' , a )
print('*' * 50)

##############################################################################################

# Generator expression 
# Creating generator object just like list comprehension

list_variable = [1,2,3,4,5]
generator_object = (i ** 2 for i in list_variable)
# Wait a min , So using '()' does not create tuple comprehension ?
# Tuples are immutable so we can't assign them new values , 
# so there is no Tuple comprehension in Python

print('generator_object : ' , generator_object)
print('List of generator object :' , list(generator_object))
print('*' * 50)

##############################################################################################

# As function can be passed inside on another , Generators can do same too
def add_3(number):
    value = number + 3
    yield value

def add_5(number):
    value = number + 5
    yield value

value = sum(add_3(sum(add_5(2))))
print('2 + 3 + 5 :' , value)

# So why we use sum() BIF ?
# Unlike return keyword , yield will give generator object 
# we can't do any operation on them unless we convert them to basic data types
print('*' * 50)

##############################################################################################
