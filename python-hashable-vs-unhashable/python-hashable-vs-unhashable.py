

# String is hashable so hash function gives proper response
string_variable = 'abc'
print('String variable hash value :' , hash(string_variable))

# list is unhashable so hash function does not gives proper response
list_variable = [1,2,3]
print('List variable hash value :' , hash(list_variable))

##############################################################################################
