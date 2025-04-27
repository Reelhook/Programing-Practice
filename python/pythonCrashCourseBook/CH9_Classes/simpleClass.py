class Dog:
    """A simple attempt to model a Dog"""

    def __init__(self, name, age):
        """Intialize name and age of attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to  command"""
        print(f"{self.name} is now sitting")

    def rollOver(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")


my_dog = Dog("Gunner", 5)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")


print("")
