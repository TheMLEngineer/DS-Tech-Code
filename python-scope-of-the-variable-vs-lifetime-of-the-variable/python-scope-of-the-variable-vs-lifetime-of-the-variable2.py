def my_function():
    local_var = 20
    print(local_var)

my_function() # Output: 20
print(local_var) # Raises an error: NameError: name 'local_var' is not defined
