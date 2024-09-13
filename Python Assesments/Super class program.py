class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Speak method must be implemented by subclasses")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class MyAnimal(Animal):
    def speak(self):
        super().speak()  
        print("I'm a custom animal!")


dog = Dog("Buddy")
cat = Cat("Whiskers")
my_animal = MyAnimal("Fluffy")


dog.speak()
cat.speak()
my_animal.speak()