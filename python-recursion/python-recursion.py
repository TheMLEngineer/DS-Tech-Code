# Recursion
def function(number):
    # Base Condition
    if number >= 3:
        return 'Number has reached required value 3'
    # Here we call function inside function
    else:
        # printing number here so we can follow what changes are happening to number variable
        print(number)
        # Here the process we do is same , we add 1 to given number
        return function(number + 1)

print(function(0))
