import pickle
dictionary = {'Key 1' : 'Value 1' , 'Key 2' : 'Value 2' , 'Key 3' : 'Value 3'}

# The Actual Value
print('The Actual Dictionary Value :' , dictionary)
print('*' * 50)
# Serialization , Object to Byte stream
pickled_object = pickle.dumps(dictionary)
print('This is the Pickled Dictionary Value :' , pickled_object)
print('*' * 50)

# Deserialization , Byte stream to Object
unpickled_object = pickle.loads(pickled_object)
print('This is the Unpickled Dictionary Value :' , unpickled_object)
print('*' * 50)