class Dog:
    """A simple attampt to model a dog"""
    def __init__(self,name,age) -> None:
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simlate rolling over in response to a command"""
        print(f"{self.name} rolled over")

my_dog = Dog('willie',6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")