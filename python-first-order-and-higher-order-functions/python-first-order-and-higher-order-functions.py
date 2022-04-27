# First Order Function
def print_function(string_to_print):
    print(string_to_print)
print_function('Hello World')


##############################################################################################


# Higher Order Function that takes function as input
def print_function(string_to_print):
    print(string_to_print)
def second_print_function(string_to_print , print_function):
    print('*' * 10)
    print_function(string_to_print)
    print('*' * 10)
second_print_function('Hello World' , print_function )


##############################################################################################

# Higher Order Function that returns function as output
def return_3():
    return 4
def return_return_3():
    return return_3()
print(return_return_3())

##############################################################################################
