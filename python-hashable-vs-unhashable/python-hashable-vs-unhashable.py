
# String is hashable so hash function gives proper response
string_variable = 'abc'
print('String variable hash value :' , hash(string_variable))

# All functions in Python is hashable
def fn():
  print('Hi')
print('Hash Value of a function :' , hash(fn))

# list is unhashable so hash function does not gives proper response
list_variable = [1,2,3]
print('List variable hash value :' , hash(list_variable))



##############################################################################################
