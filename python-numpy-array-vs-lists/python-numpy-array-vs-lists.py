import numpy as np
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
    nparr = np.append(numpy_array_data , [i])
end_time = datetime.now()
print('Appending in Numpy Array Duration: {}'.format(end_time - start_time))



##############################################################################################

import numpy as np
import sys

print('Size of 1 element list :' , sys.getsizeof([1]))
print('Size of 1 element numpy array :' , sys.getsizeof(np.array([1])))

##############################################################################################


# numpy array vs list
# Numpy can only be homogenous
import numpy as np
np_array = np.array(['1' , 2 , 3.3])
print('All values are now in string dtype :' , np_array)

##############################################################################################

import numpy as np
# Directly used for numerical operations
list_1 = [1,2,3]
numpy_1 = np.array(list_1)

print('List * 3 :' , list_1 * 3)
print('Numpy Array * 3:' , numpy_1 * 3)

##############################################################################################