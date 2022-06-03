# Iterable
iterable_object = [1,2,3]
# Iterator
iterator_object = iter([1,2,3])

print('iterable_object :' , iterable_object)
print('iterator_object :' , iterator_object)

##############################################################################################

my_string = "Karthik"

try:
    a = next(my_string)
except Exception as e:
    print('Exception has occured ...')
    print(e)

# Converting iterable to iterator
iterator_string = iter(my_string)
a = next(iterator_string)
print('First Value :' , a)

##############################################################################################
