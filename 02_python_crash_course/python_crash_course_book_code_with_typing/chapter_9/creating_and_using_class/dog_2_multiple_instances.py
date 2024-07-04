class Dog:
    """A simple attampt to model a dog"""

    def __init__(self,name,age):
        """initialize te name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate the dog sitting in response to a command."""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """simulate the rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('willie',6)
your_dog = Dog('lucy',3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()