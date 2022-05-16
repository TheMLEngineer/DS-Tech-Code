# Frozensets can do all operations as set , only thing is frozen sets are immutable
# Creating frozensets
fset1 = frozenset([1,2,3,4,5])
fset2 = frozenset([4,5,6,7,8])

# Using Frozenset as dictionary key
d = {}
d[fset1] = 'Value'
print('Dictionary :' , d)

# Copy
f_copy = fset1.copy()

# Union
print(fset1.union(fset2))

# Intersection
print(fset1.intersection(fset2))

# Difference
print(fset1.difference(fset2))

# Symmetric Difference
print(fset1.symmetric_difference(fset2))

# isdisjoint()
print(fset1.isdisjoint(fset2))

# issubset()
print(fset1.issubset(fset2))

# issuperset()
print(fset1.issuperset(fset2))

##############################################################################################