
class Animal:

    isMammal = True
    age = 3

    def movement(self):
        print("Animal is moving")

class Dog(Animal):
    def bark(self):
        print("woof!! woof!! woof!!")

 class cat:
     def meow(self):
        print("meow!! meow!! meow!!")

         dog1 = Dog()
         dog1.movement()
        print(dog1.age)

         cat1 = cat()
         cat1.meow()
