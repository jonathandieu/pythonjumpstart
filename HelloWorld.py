
msg = "Hello World"
print (msg.upper())

class person:
    def __init__(self, name, hair):
        self.name = name
        self.hair = hair
    
    def eat(self):
        """
        what is this?
        """
        pass
    @staticmethod
    def display():
        """
        not sure what this does
        """
        print('this person is doing something')
        pass

Jon = person("Jonathan","Black")
# print(Jon.hair)
Jon.display()
Jon.eat()
num = 12
print (float(num))