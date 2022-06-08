# Python program showing
# abstract base class work

from abc import ABC, abstractmethod

class AnimalKingdom(ABC):

	@abstractmethod
	def animal(self):
		pass

class Dog(AnimalKingdom):

	# overriding abstract method
	def animal(self):
		print("I Bark")

class Cat(AnimalKingdom):

	# overriding abstract method
	def animal(self):
		print("I Meow")

class Snake(AnimalKingdom):

	# overriding abstract method
	def animal(self):
		print("I Hissssss")



# Driver code
R = Dog()
R.animal()

K = Cat()
K.animal()

R = Snake()
R.animal()
