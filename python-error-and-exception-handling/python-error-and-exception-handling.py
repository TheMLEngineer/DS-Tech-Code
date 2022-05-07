# I added a space before print() , so this causes syntax error
 print('Hi')

##############################################################################################

# You see here the variable is printed in command line
# After syntax check python code is executed line by line and till any error or exception occurs in say line 5
# All code till line 4 will be executed successfully before program stops execution 
variable = '123'
print(variable)

# What if I try to access a file that does not exist ?

file_pointer = open('test.txt' , 'r')
file_content = file_pointer.read()
file_pointer.close()

##############################################################################################

# Custom Error
class CustomError(BaseException):
    ''' This is a custom error class '''
    def __str__(self):
        return ' A Custom error is raised'

raise CustomError


##############################################################################################

# Custom Exception
class CustomException(Exception):
    ''' This is a custom exception class '''
    def __str__(self):
        return ' A Custom exception is raised'

raise CustomException

##############################################################################################

import sys
# First Code Logic with no Erros
try:
  print("Printting Hi")
except:
  print("Exception Occured")
else:
  print("Code executed well") 
finally:
    print('This stament is printed no matter we got error / exception')
print('*' * 50)

# Second code logic with Errors
try:
  raise ZeroDivisionError
except:
  print("This Exception has Occured :" , sys.exc_info()[0])
else:
  print("Code executed well") 
finally:
    print('This stament is printed no matter we got error / exception')

##############################################################################################
