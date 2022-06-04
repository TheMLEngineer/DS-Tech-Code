

from datetime import datetime

list_data = [1,2,3]
numpy_array_data = np.array(list_data)
list_data = [1,2,3]

start_time = datetime.now()
# Appending in list
for i in range(100000):
    list_data.append(i)
end_time = datetime.now()
print('Appending in list Duration: {}'.format(end_time - start_time))


start_time = datetime.now()
# Appending in Numpy Array
for i in range(100000):
    nparr = np.append(nparr , [i])
end_time = datetime.now()
print('Appending in Numpy Array Duration: {}'.format(end_time - start_time))



##############################################################################################




##############################################################################################




##############################################################################################




##############################################################################################




##############################################################################################




##############################################################################################
