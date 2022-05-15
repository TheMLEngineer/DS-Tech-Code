
# Opening the file and check it's encoding
# Creating a new file

f = open('test.txt' , 'w')
# As I am running this from linux it gives encoding as UTF-8
print('Encoding of this file :' , f.encoding)
# Closing file pointer
f.close()

##############################################################################################

import os

# CRUD Operations on Files

# If we use with , no need to manually close file pointer
file_pointer =  open('new_file.txt' , 'a+')
# Writing in file
for i in range(1 , 4):
    print(f'This is line number {i}\n')
    file_pointer.write(f'This is line number {i}\n')

# Reading from file
# Reading as string
string_in_file = file_pointer.read()
# Reading as list
list_in_file = file_pointer.readlines()
print('String content in new_file.txt :' , string_in_file)
print('List content in new_file.txt :' , list_in_file)

# Update Content In File
l = []
for line in list_in_file:
    l.append(line.replace('This is' , 'This is updated '))
    file_pointer.write('\n'.join(l))

    
# Deleting File content
with open('new_file.txt' , 'w') as fp:
    # Deleting all new line characters
    for line in list_in_file:
        if 'This' in line:
            fp.write(line)

# Deleting file itself
#os.remove('new_file.txt')



    













##############################################################################################

##############################################################################################

##############################################################################################

##############################################################################################