# Welcome to Python in Visual Studio Code!
# Click the green Run button in the top right corner
# of this editor to run your first Python program.
print("Hello world!")

class Test(object):
    """
    This must be for documentation: it's a docstring
    it works in multiple lines too
    """
    weight = 0
    difficulty = 0
    def show(self):
        """
        This method prints out what values are in the object.
        """
        print(self.weight)
        pass
    pass

final = Test()
final.show()

class myClass():
    """
    This is a class that does nothing
    """
    x = 4
    def myMethod(self):
        print("this")

class myOtherClass(myClass):
    """
    This is a class that does nothing
    """
    def myMethod(self):
        print("that")

x = myOtherClass()
x.myMethod()