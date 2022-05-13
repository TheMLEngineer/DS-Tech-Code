name = 'Karthik'
age = 24

# f-string using 'f'
print(f'I am {name}')

# f-string using 'F'
print(F'I am {name}')

# Multiline f-string
data = (
    f"I am {name}"
    F"\nMy Age is {age}"
)
print('Multiline f-string :')
print(data)

# Expressions inside f-string
print(f'3 + 5 = {3+5}' )


##############################################################################################

import datetime
today = datetime.datetime.today()
# Using f-string for time formatting
print(f"{today:%B %d, %Y}")

##############################################################################################

# Call Functions Inside f-string
def fn():
    print('Function is called ...')
# Here we are not even assigining f-string to a variable
# We just run f-string , it is not stored , but
# expression inside fstring gets executed
F'{fn()}'

##############################################################################################