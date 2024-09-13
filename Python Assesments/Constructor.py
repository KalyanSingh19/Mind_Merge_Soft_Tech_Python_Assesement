#In object-oriented programming, a constructor is a special method that is automatically called when an object of a class is created.


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

# Creating a Dog object
my_dog = Dog("Rocky", "Rotweiler")

# Accessing the attributes
print(my_dog.name)  
print(my_dog.breed)  