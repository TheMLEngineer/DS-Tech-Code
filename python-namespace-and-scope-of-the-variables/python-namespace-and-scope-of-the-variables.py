# Namespace and Scope
# Built In Scope
# Whenever Python interpreter loads all names in builtin scope are automatically loaded
scope_variable = dir(__builtins__)
print('Number of Built in Names loaded are :' , len(scope_variable))
print('Whenever Python interpreter loads all names in builtin scope are automatically loaded')
print('*'*50)

# This is global scope
scope_variable = 3
print('Scope Variable in Global :' , scope_variable)
print('*'*50)

def first_function():
    scope_variable = 4
    # This is enclosed scope
    print('Scope Variable in Enclosed :' , scope_variable)
    print('*'*50)

    def second_function():
        # This is local scope
        scope_variable = 5
        print('Scope Variable in Local :' , scope_variable)
        print('*'*50)

    second_function()

first_function()
