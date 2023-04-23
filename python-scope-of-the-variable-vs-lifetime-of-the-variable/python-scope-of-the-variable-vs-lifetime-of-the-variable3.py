def outer_function():
    outer_var = 30
    def inner_function():
        nonlocal outer_var
        print(outer_var)
    inner_function()

outer_function() # Output: 30
