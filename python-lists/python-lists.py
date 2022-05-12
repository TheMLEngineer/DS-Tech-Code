
# List Basics
# CRUD Operations on list
# Creating an empty list
list_variable = []
print(list_variable)
print('*'*50)
# Adding values to list without using built in methods
list_variable = list_variable + [1,2]
print(list_variable)
print('*'*50)
# Reading every element from list
for element in list_variable:
    print(element)
print('*'*50)
# Deleting First List element
del list_variable[0]
print(list_variable)
print('*'*50)
# What if we use * on Lists
# if we multiply by 1 or higher list elemensts are duplicated that many times
print([1,2] * 2)
# If we multiply by 0 or -ve numbers , empty list is returned
print([1,2] * -2)
print('*'*50)


##############################################################################################

# List Iteration
# List Iterate
list_variable = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
print('Original List content at begining :' , list_variable)
print('*'*50)
# Using for loop
print('Iteration Using for loop')
for element in list_variable:
    print(element)
print('*'*50)
# Using while loop
print('Iteration Using while loop')
while len(list_variable) != 0:
    first_element = list_variable.pop(0)
    print(first_element)
print('*'*50)

##############################################################################################
# List Indexing And Slicing
# List Indexing
list_variable = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
print('Original List content at begining :' , list_variable)
print('*'*50)

# Accessing 'c' using Positive Indexing
print("Accessing 'c' using Positive Indexing")
print(list_variable[2])
print('*'*50)
# Accessing 'c' using Negative Indexing
print("Accessing 'c' using Negative Indexing")
print(list_variable[-4])
print('*'*50)

# List Slicing
list_variable = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
print('Original List content at begining :' , list_variable)
print('*'*50)
# Printing 'b' to 'e' using slicing
print("Printing 'b' to 'e' using slicing")
print(list_variable[1:5])
print('*'*50)

##############################################################################################
# List Comprehension
# List Comprehension
# Only having variable
list_variable = [i for i in range(10)]
print('List comprehension using only variable :' , list_variable)
print('*'*50)
# Actions on variable
list_variable = [i * i for i in range(10)]
print('List comprehension using actions on variable (Here multiplying variable with variable):' , list_variable)
print('*'*50)
# Actions and conditions on variable
list_variable = [i * i for i in range(10) if i % 2 == 0]
print('List comprehension using actions and conditions on variable (Here multiplying variable with variable if variable is even number):' , list_variable)
print('*'*50)

##############################################################################################
# List Methods

# List built in methods
# Method : Append
# What It Does : Add an item to the end of the list.
list_variable = []
list_variable.append(3)
# append method can be used to append other built in data types like sets , dictionary , tuples etc
list_variable.append({5,6,7})
print(list_variable)
print('*'*50)
# Achieveing list appending without using append() method
list_variable[len(list_variable) : ] = [44]
print(list_variable)
print('*'*50)


# List built in methods
# Method : Extend
# What It Does : Extend the list by appending all the items from the iterable.
list_variable = []
list_variable.extend([1,2,3])
# If you see in append , the whole list element is appended at the end as one item
# In extend we iterate through the iterable and add each item at the end of list
print(list_variable)
print('*'*50)
# What if we use extend function on an non iterable variable like integer ?
try:
    list_variable.extend(3)
except Exception as e:
    print('Type Error has occured while trying to use extend function on an non iterable variable like integer :' ,e)
print('*'*50)
# What happens if we try to append Nested lists ?
list_variable.extend([[4,5,6] , [7,8,9]])
# Extend only iterate though once
# So even if the element inside an iterator is an iterator it won't unpack the second iterator
print(list_variable)
print('*'*50)
# Achieveing list extending without using extend() method
list_variable[len(list_variable) : ] = [10 , 11]
print(list_variable)
print('*'*50)

# List built in methods
# Method : Insert
# What It Does : To Insert an item at a given position. 
list_variable = ['element 1' , 'element 2' , 'element 3']
# Here 0 is the index(Index can be positive index or negative index) and 'first element' is the value we are inserting
# You can insert any values like int , flot , lists , tuple etc.
list_variable.insert(0 , 'first element')
print(list_variable)
print('*'*50)
# What if index we are inserting in does not exist in list
list_variable.insert(44 , 'latest element')
# Index 44 does not exist in list
# Still insert method added the value at the end of the list
print(list_variable)
print('*'*50)

# List built in methods
# Method : Remove
# What It Does : To Remove an item in the list
list_variable = [1,2,3,2]
print('List content at begining :' , list_variable)
print('*'*50)
list_variable.remove(1)
print('List content after removing 1 :' , list_variable)
print('*'*50)
# Trying to remove a value that does not exist
try:
    list_variable.remove('Non existant value in list')
except Exception as e:
    print('When Trying to remove a value that does not exist Value Error Occured : ' , e)
print('*'*50)
# What if list has duplicate elements ?
list_variable.remove(2)
# If a list contains duplicate elements, the remove() method only removes the first matching element
print('List content after removing a duplicate element :' , list_variable)
print('*'*50)


# List built in methods
# Method : Pop
# What It Does : Pop removes the item at the given position in the list, and return it.If no index is specified, a.pop() removes and returns the last item in the list.
list_variable = [1,2,3,4]
print('List content at begining :' , list_variable)
print('*'*50)
# Popping value at index 1
popped_value = list_variable.pop(1)
print('List content after popping value at index 1 :' , list_variable)
print('Popped value :' , popped_value)
print('*'*50)
# Popping without index
# If no index is specified, a.pop() removes and returns the last item in the list.
popped_value = list_variable.pop()
print('List content after popping with no arguments :' , list_variable)
print('Popped value :' , popped_value)
print('*'*50)
# If the index passed to the method is not in range, it throws IndexError: pop index out of range exception.
try:
    # tryinh to pop value at index 1000
    popped_value = list_variable.pop(1000)
except Exception as e :
    print('IndexError: pop index out of range error occured' , e)
print('*'*50)



# List built in methods
# Method : Index
# What It Does : Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
list_variable = [1,2,3,4]
print('List content at begining :' , list_variable)
print('*'*50)
# index of element 1
index_of_1 = list_variable.index(1)
print('Index Of Element 1 in List :' , index_of_1)
print('*'*50)
# 3 parameters of list.index()
# 1) element - the element to be searched
# 2) start (optional) - start searching from this index
# 3) end (optional) - search the element up to this index
# Here we search for 1 in [3,4] , By setting up args accordingly
try:
    index_of_1 = list_variable.index(1 , 2 , -1)
except Exception as e:
    print('ValueError: 1 is not in list has occured : ' , e)
print('*'*50)





# List built in methods
# Method : Count
# What It Does : Returns the number of times an element appears in the list.
list_variable = [1,2,3,4,1,1,2,2,3]
print('List content at begining :' , list_variable)
print('*'*50)
number_of_times_one_have_occured = list_variable.count(1)
print('number_of_times_one_have_occured in the list are :' , number_of_times_one_have_occured)
print('*'*50)






# List built in methods
# Method : Sort
# What It Does : Sort the items of the list in place.
list_variable = ['a' , 'zz' , 'f' , 'hhhh' , 't']
print('List content at begining :' , list_variable)
print('*'*50)
# sort() changes the list directly and doesn't return any value
list_variable.sort()
print('List content after using sort() :' , list_variable)
print('*'*50)
# Using reverse argument
list_variable.sort(reverse=True)
print('List content after using sort() with reverse as True :' , list_variable)
print('*'*50)
# Using key argument (It accepts a function as key and sorts based on the key function)
# Here we'll use built in len function

list_variable.sort(key = len)
print('List content after using sort() with len() key function :' , list_variable)
print('*'*50)










# List built in methods
# Method : Reverse
# What It Does : Reverse the elements of the list in place.
list_variable = [4,7,2,4,6,7,8,98,3]
print('List content at begining :' , list_variable)
print('*'*50)
# Using reverse()
# reverse() changes the list directly and doesn't return any value
list_variable.reverse()
print('List content after using reverse() :' , list_variable)
print('*'*50)
# Reverse method does not sort descending , It just reverses the values in list in opposite order






# List built in methods
# Method : Clear
# What It Does : Clear Remove all items from the list
list_variable = [1,2,3,4]
print('List content at begining :' , list_variable)
print('*'*50)
list_variable.clear()
print('List content after clear() method :' , list_variable)
print('*'*50)


# List built in methods
# Method : Copy
# What It Does : Return a shallow copy of the list
list_variable = [1,2,3]
print('Original List content at begining :' , list_variable)
print('*'*50)
copy_of_list = list_variable.copy()
copy_using_equal_sign_list = list_variable
print('Original List content after copying :' , list_variable)
print('Copied List content using copy() : ' , copy_of_list)
print('Copied List content using "=" sign : ' , copy_using_equal_sign_list)
print('*'*50)
# Changing values in both copied lists
copy_of_list.append(3)
copy_using_equal_sign_list.append(4)
print('Original List content after appending 4 :' , list_variable)
print('Copied List content using copy() after appending 3 : ' , copy_of_list)
print('Copied List content using "=" sign after appending 4 : ' , copy_using_equal_sign_list)
print('*'*50)
# We can understand that if we do copy using = sign if we change the copied list content , original list content also changes
# But in .copy() the original list content does not change even if you change the copied list content.
print('''We can understand that if we do copy using = sign if we change the copied list content , original list content also changes. But in .copy() the original list content does not change even if you change the copied list content.
''')
print('*'*50)

##############################################################################################
