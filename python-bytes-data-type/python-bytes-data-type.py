
# Bytes
# Byte Object Creation
byte_object = bytes([ 1, 2 , 3])
print('Byte Object :' , byte_object)

# Bytes can only represent values from 0 to 255
try:
    new_byte_object = bytes([1 , 2 , 256])
except Exception as e:
    print('This Error Occured :' , e)

# Byte Objects are immutable
try:
    byte_object[0] = 'New Value'
except Exception as e:
    print('This Error Occured :' , e)

# Type Conversion
# String To Byte
string_variable = 'string'
byte_variable = bytes(string_variable , encoding= 'utf-8')
print('Byte Variable :' , byte_variable)

# Byte To String
decoded_string_variable = byte_variable.decode()
print('Decoded String Variable :' , decoded_string_variable)

##############################################################################################

# Byte Arrays
# Byte Arrays Object Creation
byte_array_object = bytearray([1 , 2 , 3])
print('Byte Array Object :' , byte_array_object)

# byte arrays are same as bytes object but byte arrays are mutable
byte_array_object[0] = 55
print('Byte Array Object after changes :' , byte_array_object)

# Bytes arrays also can only represent values from 0 to 255
try:
    new_byte_object = bytearray([1 , 2 , 256])
except Exception as e:
    print('This Error Occured :' , e)

type(byte_array_object)

##############################################################################################