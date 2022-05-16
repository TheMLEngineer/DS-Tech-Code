
# Tuples

t1 = (1,'2',3+4j , 'Hello' , 'Elon')
print(type(t1))

# Indexing and Slicing
print(t1[2])
print(t1[::2])


# Editing List Inside Tuple
t2 = (1,2,['Hi'])
print('Tuple Value before changing :' , t2)
t2[2].append('Hello')
print('List inside tuple is changed now :' , t2)

# Adding tuples
print(t1 + t2)

# Multiplying tuples
print(t2 * 3)

# Built In Methods
print(t1.count('Elon'))
print(t1.index('Elon'))

# Iterating
for element in t1:
    print(element)

# Membership Test
print('Elon' in t1)

# As tuple is immutable , we can edit tuple by converting into list and doing list operations

##############################################################################################