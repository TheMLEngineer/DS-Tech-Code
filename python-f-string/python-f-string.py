

name = 'Karthik'
age = 24

# f-string using 'f'
print(f'I am {name}')

# f-string using 'F'
print(F'I am {name}')

# Multiline f-string
data = (
    f"I am {name}"
    F"My Age is {age}"
)
print('Multiline f-string :')
print(data)

# Expressions inside f-string
print(f'3 + 5 = {3+5}' )

##############################################################################################

import datetime
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

##############################################################################################

# Call Functions Inside f-string
def fn():
    print('Function is called ...')
F'{fn()}'

##############################################################################################