
byte_array_object = bytearray([1 , 2 , 3])
# a bytes-like object is required to pass into memoryview()
memory_view_object = memoryview(byte_array_object)
print('Type of memoryview object :' , type(memory_view_object))

# Access memory
print('memory view object on zero index : ' , memory_view_object[0])
# Type conversion
print('memory view to list :' , list(memory_view_object))

# Updating zero index value to 33 using memoryview
memory_view_object[0] = 33
print('memory view object after updating memory_view_object : ' , list(memory_view_object))

# If we update actual bytearray we pass inside that update reflects in memoryview also
# Coz memory_view_object reference the same memory
byte_array_object[1] = 22
print('memory view object after updating byte_array_object : ' , list(memory_view_object))

##############################################################################################

import timeit

#Increasing data size
bytes_data = b'Sample String' * 5000
# Code logic for deleting first index value of given data repeatedly
bytes_time = timeit.timeit('while bytes_data: bytes_data = bytes_data[1:]', "from __main__ import bytes_data")
memory_view_data = memoryview(bytes_data)
memory_view_time = timeit.timeit('while memory_view_data: memory_view_data = memory_view_data[1:]', "from __main__ import memory_view_data")


print('Without memory view how much time it took :' , bytes_time)
print('With memory view how much time it took :' , memory_view_time)


##############################################################################################