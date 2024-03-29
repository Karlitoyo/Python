"""
Simple Class by JOR, by convention, use camel case to name classes
"""

# Create a class 
class JORzClass():
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for JORzClass")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)

my_class1 = JORzClass("Morning JOR!")
my_class1.my_method()
print(type(my_class1))

# Create another instance of JORzClass called MyClass2
my_class2 = JORzClass("Hello JOR!")
my_class2.my_method()
print(type(my_class2))