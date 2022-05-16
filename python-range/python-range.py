
# Range

print('range() document :' , range.__doc__)

# Positive Step Size
range_object = range(1 , 11 ,  1)
list_of_elements = list(range_object)
print('Using list() to get values from range object :' , list_of_elements)

# Using negative step size
range_object = range(15 , 1 ,  -1)
list_of_elements = list(range_object)
print('Using list() to get values from range object (Negative Step Size):' , list_of_elements)

##############################################################################################