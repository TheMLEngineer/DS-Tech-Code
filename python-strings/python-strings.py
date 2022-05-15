# Strings
# CRUD on Strings

# Created String
print('Creating String ...')
string = '  This is an example string  '

# Reading String
print("Reading String ... ")
for character in string:
    print(character , end = '')

# Updating String Element
# As String is immutable we use a one / combination of these methods to update string
# Slicing , Copying , Indexing , Built in string methods
words = string.split(' ')
new_string = ''.join(words[::-1])
print(f'\nUpdated String Is : {new_string}')

# Deleting String
# If tried to delete part of string / one character from string it raises error as string is immutable
try:
    del new_string[0]
except Exception as e:
    print('Error occured while deleting part of string :' , e)

# However we can delete whole string variable
del new_string


##############################################################################################

# String Methods
s = 'the quick brown FOX jumps over the lazy dog   '
print('Actual String :' , s)
print('Capitalized String :' , s.capitalize())
print('Lower Case String :' , s.lower())
print('Upper Case String :' , s.upper() )
print('Swapping Case Of String :' , s.swapcase())
print('Title Case :' , s.title())

# Searching and replacing
print('Index of value "q" :' , s.find('q'))
print('Replacing "s" with "sss" :' , s.replace('s' , 'sss'))

# Checking types
print('Is string alphanumeric ? ', s.isalnum())
print('Is string Alpha ? ' , s.isalpha())
print('Is string digit ? ' , s.isdigit())
print('Is the string a valid identifier ? ' , s.isidentifier())
print('Is string already in lower case ? ' ,s.islower())
print('Is string already in upper case ? ' ,s.isupper())
print('Is string printable ? ' , s.isprintable())

# Formatting
# Returning a String in a centered field
print('Centerred String :' , s.center(10))
print('Stripped of spaces :' , s.strip())
s = s.strip()

# Joining
l = list(s)
joined_string = '\t'.join(l)
print('Joined String :' , joined_string)

# Split string
print('Using Partition :' , s.partition('fox'))
print('Using Split :' , s.split(' '))

# Counting
print('Number of times "j" occur in string :' , s.count('j'))
print('Does string endswith "a" ? ' , s.endswith('a'))
print('Does string startswith "t" ? ' , s.startswith('t'))

##############################################################################################