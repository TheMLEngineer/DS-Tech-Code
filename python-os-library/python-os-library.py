
import os

# Name of OS Module
print('Name Of OS Module:' , os.name)

# Checking if dir exist
if os.path.exists('dir'):
    print('dir folder already exist ...')
else:
    # If does not exist Creating New Directory
    os.mkdir('dir')
    print('Dir name "dir" is created ...')

# Get current working directory
print('Current Working Directory :' , os.getcwd())

# Change Directory
# As we already created 'dir' directory , will switch there
os.chdir('dir')
print('After changing to dir , Current Working Directory :' , os.getcwd())

#Changing back to HOME Dir
os.chdir('../')

# Delete dir
os.rmdir('dir')
print('Deleted dir folder')

# Create file
with open('text.txt' , 'w') as f:
    pass
# Change File Name
print('Changing File Name ...')
os.rename('text.txt' , 'new_text.txt')


# Folder content
content = os.listdir()
print('Files and Directories in Current Folder :' , content)


##############################################################################################