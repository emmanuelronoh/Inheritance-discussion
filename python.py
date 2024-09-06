#Example of inheritance using single and multiple inheritance

class Mammal:
    def walk(self):
        print("walk")

class Animal:
    def give_birth(self):
        print("give birth")


class Dog(Mammal, Animal):
    pass


class Cat(Mammal, Animal):
    pass

dog1 = Dog()
dog1.walk()
dog1.give_birth()
cat1 = Cat()
cat1.walk()