class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass


animals = [
    Animal('lion'),
    Animal('mouse')]


def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')

        elif animal.name == 'mouse':
            print('squeak')


animal_sound(animals)

"""
The function animal_sound does not conform to the open-closed principle because it cannot be closed against new kinds 
of animals.
If we add a new animal, Snake, We have to modify the animal_sound function.
You see, for every new animal, a new logic is added to the animal_sound function. 
"""

animals = [
    Animal('lion'),
    Animal('mouse'),
    Animal('snake')
]


def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('squeak')
        elif animal.name == 'snake':
            print('hiss')


animal_sound(animals)

"""
How do we make it (the animal_sound) confirm to OCP
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animal_sound(animals)

"""
Animal now has a virtual method make_sound. We have each animal extend the Animal class and implement the virtual make_sound method.
Every animal adds its own implementation on how it makes a sound in the make_sound. 
The animal_sound iterates through the array of animal and just calls its make_sound method.
Now, if we add a new animal, animal_sound doesn’t need to change. 
All we need to do is add the new animal to the animal array.
"""
