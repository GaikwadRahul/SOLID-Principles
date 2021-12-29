"""
A class should have only one job.
If a class has more than one responsibility, it becomes coupled.
A change to one responsibility results to modification of the other responsibility.
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass


"""
The Animal class violates the SRP.

SRP states that classes should have one responsibility, here, we can draw out two responsibilities: animal database 
management and animal properties management. 
If the application changes in a way that it affects database management functions. The classes that make use of Animal 
properties will have to be touched and recompiled to compensate for the new changes.
To make this conform to SRP, we create another class that will handle the sole responsibility of storing an animal to 
a database:
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self) -> Animal:
        pass

    def save(self, animal: Animal):
        pass
