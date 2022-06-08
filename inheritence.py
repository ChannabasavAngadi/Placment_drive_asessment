class Animal:
    def speak(self):
        print("Animal Speaking")
    # child class Dog inherits the base class Animal


class Dog(Animal):
    def bark(self):
        print("dog barking")


class Cat(Dog):
    def Meow(self):
        print("Cat talking")

# creting object for cat
# cat inheriting dog
# dog inheriting speak
d = Cat()
d.Meow()
d.bark()
d.speak()
