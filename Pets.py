# Constructor Class
class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

# Parent Class
class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

""" Class inherited from class Cat. Notice that Class Cat gets
passed as an argument. That is an example of class Simon inheriting args
from Cat and passing them onto class Simon."""
class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Felix(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('Simon', 4), Sally('Sally', 21), Felix('Suzy', 1)]

#3 Instantiate the Pet class with all your cats
my_pets = Pets(my_cats)

#4 Output all of the cats singing using the my_pets instance
my_pets.walk()