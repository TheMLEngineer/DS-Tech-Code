
# How Python Stores A Variable

# reference count of 3 = 1
a = 3
# reference count of 3 = 2
b = 3

# Both a and b are pointing to same memory location
print(id(a))
print(id(b))


# reference count of 3 = 1
del a
# reference count of 3 = 0
del b

# After deleting both the references to 3 , 3 will be garbage collected

##############################################################################################

def function():
    # a is allocated on stack memory
    # All variables inside function is stored on stack memory
    # stack memory is deleted once the function returns (even if returns None)
    a = 3
    return a

# x is allocated on heap memory
# heap memory is bigger compared to stack memory coz all global scope variables are stored in heap memory
x = function()
print(x)

##############################################################################################