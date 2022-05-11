# Example Class
class Dinosours:
    pass

##############################################################################################
class Dinosours:
    # eyes is Static Variable
    eyes = 2
    def __init__(self , teeth):
        self.teeth = teeth
obj = Dinosours(40)
# Teeth is Instance Variable
print('Teeth :' , obj.teeth)

##############################################################################################

# A custom class can inherit methods from Built in class (Here we inherit list class)
class C1(list):
    pass
obj = C1()
obj.append(33)
print('Appended element by inheriting list object :' , obj)

##############################################################################################

# Check sample.py for code logic
from sample import Sample
# While creating object itself init method would have been called , so without any print() the current path of main.py is printed
s = Sample()

##############################################################################################