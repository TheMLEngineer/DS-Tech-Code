
# map
# fn to return True if string starts with 'A'
function1 = lambda x : x.startswith('A')
iterable1 = ['Apple' , 'Banana' , 'Aeroplane']
map_object = map(function1 , iterable1)
print('Map object :' , list(map_object))

# filter
# fn to return True if number is even
function2 = lambda x : x % 2 == 0
iterable2 = [3 , 4 , 8]
filter_object = filter(function2 , iterable2)
print('Filter object :' , list(filter_object))

# reduce
from functools import reduce
# fn to add two numbers
function3 = lambda a , b : a + b
iterable3 = [3 , 4 , 8]
reduce_object = reduce(function3 , iterable3)
print('Reduce object :' , reduce_object)

##############################################################################################