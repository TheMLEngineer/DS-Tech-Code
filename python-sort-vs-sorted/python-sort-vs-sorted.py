list_variable = [3,5,1,2,4]

# Using sorted()
print('Using sorted() built in function : ')
print('Actual List content before sorting :' , list_variable)
print('Sorted() :' , sorted(list_variable))
print('Now printing the list content again :' , list_variable)
# Seems sorted() does not change the actual list object content

print('*' * 50)
# Using list.sort()
print('Using list.sort() built in list method : ')
print('Actual List content before sorting :' , list_variable)
print('list.sort() :' , list_variable.sort())
print('Now printing the list content again :' , list_variable)
# Seems list.sort() stored the sorted list content in the passed list object