# Creating set with unhashable element(list) inside will create TypeError
print('Creating set with unhashable element :' , {[1,2,3]})

##############################################################################################
# Creating sets
set1 = {1,1,1,1,2,3,4}
print('set1 :',set1)
set2 = {3,4,4,4,4,5}
print('set2 :',set2)

# Add elements to set
print('Set 1 before adding element :' , set1)
set1.add('new element')
print('Set 1 after adding element :' , set1)

# Delete elements of set
# .remove() raises exception if deleted element not exist in set , 
# so we use .discard() here which does not raise any exceptions even if passed element is not part of set 
print('Set 1 before deleting element :' , set1)
set1.discard('new element')
print('Set 1 after deleting "new element" element :' , set1)

# Reading all set elements
print('Reading all set elements ...')
for element in set1:
    print(element , end = '\n')

# Set union
union_set = set1 | set2
print('union set :' , union_set)

# Set Intersection
intersection_set = set1 & set2
print('intersection set :' , intersection_set)

# Set difference
difference_set = set1 - set2
print('difference set :' , difference_set)

# Set symmetric difference
symmetric_difference_set = set1 ^ set2
print('symmetric difference set :' , symmetric_difference_set)

# isdisjoint() , Checks if two sets have any elements in common
# returns True if no common elements , false otherwise
is_disjoint = set1.isdisjoint(set2)
print('is_disjoint result :' , is_disjoint)

# issubset() , checks if one set is subset of another
is_subset = set1.issubset(set2)
print('Is set1 a subset of set2 :' , is_subset)

# issuperset() , checks if one set is superset of another
is_superset = set1.issuperset(set2)
print('Is set1 a superset of set2 :' , is_superset)

##############################################################################################

# Frozen Sets
f_set1 = frozenset([1,2,3])
f_set2 = frozenset([3,4,5])

# Set union in frozenset
print(f_set1 | f_set2)
# Won't be able to add elements as frozenset is immutable
f_set1.add(3)

##############################################################################################
