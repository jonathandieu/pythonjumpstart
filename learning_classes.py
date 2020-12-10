# Welcome to Python in Visual Studio Code!
# Click the green Run button in the top right corner
# of this editor to run your first Python program.
print("Hello world!")

class Test(object):
    """
    This must be for documentation
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

