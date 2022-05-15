
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

f = open("demofile.txt", "a+")
# Writing in file
# Just writing into file
f.write("Adding more content!\n")

# Reading from file
# Reading as list
f.seek(0)
list_in_file = f.readlines()
print('List content in demofile.txt :' , list_in_file)

# Update Content In File
l = []
for line in list_in_file:
    l.append(line.replace('Adding' , 'This is updated '))
    f.write('\n'.join(l))

f.close()
# Deleting File content
with open('demofile.txt' , 'w') as fp:
    # Deleting all new line characters
    for line in list_in_file:
        if 'This' in line:
            fp.write(line)

#Deleting file itself
os.remove('demofile.txt')

##############################################################################################