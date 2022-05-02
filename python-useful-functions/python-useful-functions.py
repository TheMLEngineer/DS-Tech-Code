# isinstance function
# Used to check data type
print('isinstance function returns True if the value and datatype passed match if not it returns False')
print("Checking if 'a' is of String type :" , isinstance('a' , str))
print('*'*50)
# As isinstance function returns boolean True or False it can be used in conditional statement
if isinstance('a' , str):
    print("'a' is of string type")
else:
    print("'a' is not string type")
print('*'*50)
##############################################################################################
# sys.stdout
import sys
sys.stdout.write('gfg')
sys.stderr.write('ABC')

##############################################################################################
print(locals())
print(globals())
##############################################################################################
# dir()
set_variable = {}
# Here dir() will print all methods and attributes of set datatype in list format
print(dir(set_variable))
##############################################################################################
# zip()
numers = [1,2,3]
names = ['Rocky' , 'IP Man' , 'Bruce Lee']
zip_object = zip(numers , names)
print('The actual zip object :' , zip_object)
print('*'*50)

# The zip object will be an iterator , so we need to change it to list to view the zipped elements
print('List of zip object :' , list(zip_object))
print('*'*50)

# What if length of iterables we pass in zip() is not equal
numbers = [1,2,3,4,5]
names = ['Rocky' , 'IP Man' , 'Bruce Lee']
zip_object = zip(numers , names)
print('So if len(list1) is 3 and len(list2) is 5 , Only first 3 elements from each list will be taken to make a zip object')
print('List of zip object (with uneven input list length) :' , list(zip_object))
print('*'*50)
##############################################################################################
# enumerate
names = ['Rocky' , 'IP Man' , 'Bruce Lee']

# enumerate applied directly
enumerate_object = enumerate(names)
print('Enumerate applied directly :' , list(enumerate_object))
print('*'*50)

# enumerate applied in for loop
for index , value in enumerate(names):
    print('Index is :' , index)
    print('Value is :' , value)
print('*'*50)

##############################################################################################

print(eval('1+2.2'))
exec("print('Hi')")

##############################################################################################