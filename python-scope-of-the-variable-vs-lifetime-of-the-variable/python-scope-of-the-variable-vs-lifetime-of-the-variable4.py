class MyClass:
    class_var = 40

    def print_class_var(self):
        print(MyClass.class_var)

obj1 = MyClass()
obj2 = MyClass()
obj1.print_class_var() # Output: 40
obj2.print_class_var() # Output: 40
