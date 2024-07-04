class Dog:
    """A simple attampt to model a dog"""
    def __init__(self,name,age):
        """initialize the name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """simulate rolling over in response to a command."""
        print(f"{self.name} rolled over")
    
my_dog = Dog('willie',6)
my_dog.sit()
my_dog.roll_over()