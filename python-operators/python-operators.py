

# Arithmatic Operators
a = 3
b = 5

print('a value :' , a)
print('b value :' , b)
print('a + b :' , a + b)
print('a - b :' , a - b)
print('a * b :' , a * b)
print('a / b :' , a / b)
print('a % b :' , a % b)
print('a ** b :' , a ** b)
print('a // b :' , a // b)

##############################################################################################

# Comparison Operators

a = 3
b = 5

print('a value :' , a)
print('b value :' , b)
print('Is a < b ? ' , a < b)
print('Is a > b ? ' , a > b)
print('Is a <= b ? ' , a <= b)
print('Is a >= b ? ' , a >= b)
print('Is a == b ? ' , a == b)
print('Is a != b ? ' , a != b)



##############################################################################################

# Logical Operators

a = True
b = False

print('a value :' , a)
print('b value :' , b)
print('a and b : ' , a and b )
print('a or b : ' , a or b)
print('not(a and b)? ' , not(a and b))



##############################################################################################



# Bitwise Operators

a = 3
b = 4

print('a value :' , a)
print('b value :' , b)

print('a & b :' , a & b)
print('a | b :' , a | b)
print('~a :' , ~a)
print('a ^ b :' , a ^ b)
print('a >> b :' , a >> b)
print('a << b :' , a << b)



##############################################################################################


# Identity Operators

a = [3 , 5]
b = [3 , 5]
c = a

# This will return TRUE as a and b refer to same object in same memory location
print('a is c :' , a is c)

# This will return False as even though a and b has same value , they are not in same memory location
print('a is b :' , a is b)

# But a == b will return True as , == checks for value but is operator checks for object and memory location
print('a == b :' , a == b)

# is not operator , this will return True
print('a is not b :' , a is not b)




##############################################################################################


# Membership operators

l = [3 , 5 , 7]

print('Is 3 in list ? ' , 3 in l)
print('Is 8 not in list ? ' , 8 not in l)



##############################################################################################

# Assignment Operators


a = 3
print('a value after assignment :' , a)

a += 5
print('a value after +=5 :' , a)

a -= 5
print('a value after -=5 :' , a)

a *= 5
print('a value after *=5 :' , a)

a /= 5
print('a value after /=5 :' , a)

a %= 5
print('a value after %=5 :' , a)

a //= 5
print('a value after //=5 :' , a)

a **= 5
print('a value after **=5 :' , a)

# As current a value is in float , converting it to integer
a = int(a)

a &= 5
print('a value after &=5 :' , a)

a |= 5
print('a value after |=5 :' , a)

a ^= 5
print('a value after ^=5 :' , a)

a >>= 5
print('a value after >>=5 :' , a)

a <<= 5
print('a value after <<=5 :' , a)






##############################################################################################






##############################################################################################

