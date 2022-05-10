
# Using dictionary to associate data

d = dict()
d[(1,2)] = 3
print(d)

##############################################################################################

# As list datatype is not hashable it can't be a key in dictionary

d = dict()
d[[1,2]] = 3
print(d)

##############################################################################################

# Dictionary CRUD Activities

# Creating empty dictionary
dictionary_variable = {}
print('Dictionary value after Creation :' , dictionary_variable)
print('*' * 50)

# Updating value
dictionary_variable['key 1'] = 'value 1'
dictionary_variable['key 2'] = 'value 2'
print('Dictionary value after Updating :' , dictionary_variable)
print('*' * 50)

# Reading value
print('Getting Value of key 1 :' , dictionary_variable['key 1'])
print('Dictionary value after Reading one value :' , dictionary_variable)
print('*' * 50)

# Deleting in dictionary
del dictionary_variable['key 2']
print('Dictionary value after deletion of key 1 :' , dictionary_variable)
print('*' * 50)

##############################################################################################

# Dictionary methods
# Creating empty dictionary
dictionary_variable = {}
print('Dictionary value after Creation :' , dictionary_variable)
print('*' * 50)


# Updating value
dictionary_variable['key 1'] = 'value 1'
dictionary_variable['key 2'] = 'value 2'
dictionary_variable['key 3'] = 'value 3'
print('Dictionary value after Updating :' , dictionary_variable)
print('*' * 50)


# Copying dictionary
copy_dict = dictionary_variable.copy()
print('Copied dictionary :' , copy_dict)
print('*' * 50)


# Getting value using .get()
value = dictionary_variable.get('key 2')
print('Value got using get() :' , value)
print('*' * 50)


# str()
str_value = str(dictionary_variable)
print('str() :' , str_value)
print('*' * 50)


# keys() , items() , values()
keys = dictionary_variable.keys()
print('Keys in dictionary :' , keys)
items = dictionary_variable.items()
print('Items (Key value pair) in dictionary :' , items)
values = dictionary_variable.values()
print('Values in dictionary :' , values)
print('*' * 50)


# update() , setdefault()
dictionary_variable2 = {'key 2' : 'updated value 2'}
dictionary_variable.update(dictionary_variable2)
print('After update dictionary_variable :' , dictionary_variable)
print('After update dictionary_variable2 :' , dictionary_variable2)
# setdefault() returns value if key is already present if key is not present then it inserts key with value
a = dictionary_variable.setdefault('New Key' , 'New Value')
print('Dictionary value after setdefault() :' , dictionary_variable)
print('*' * 50)


# fromkeys() 
new_dict = dict.fromkeys([1,2,3] , 'value')
print('fromkeys() new dictionary :' , new_dict)
print('*' * 50)


# pop and popitem()
pop_value = dictionary_variable.pop('key 1')
print('pop() :' , pop_value)
popitem_value = dictionary_variable.popitem()
print('popitem() :' , popitem_value)
print('Dictionary value after Popping :' , dictionary_variable)
print('*' * 50)

##############################################################################################

# Dictionary Comprehension
new_dict = {i: i*i for i in range(5)}
print('new_dict created with comprehension :' , new_dict)

# Checking if a key is in dictionary
print('Is 1 in new_dict as Key :' , 1 in new_dict)

##############################################################################################