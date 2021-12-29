"""
Liskov Substitution Principle

Let φ(x) be a property provable about objects x of type T. Then φ(y) should be true for objects y of type S where S
is a subtype of T.
More formally, this is the original definition (LISKOV 01) of Liskov’s substitution principle: if S is a subtype of T,
then objects of type T may be replaced by objects of type S, without breaking the program.
"""


class Vehicle:

    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return f"The vehicle name {self.name}"

    def get_speed(self) -> str:
        return f"The vehicle speed {self.speed}"

    def engine(self):
        pass

    def start_engine(self):
        self.engine()


class Car(Vehicle):

    def start_engine(self):
        pass


class Bicycle(Vehicle):

    def start_engine(self):
        pass


"""
In Bicycle class violates the LSP. Cause in the Vehicle class has an engine method. But naturally, a bicycle has
no engine. So we could not start any engine.
"""


class Vehicle:

    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return f"The vehicle name {self.name}"

    def get_speed(self) -> str:
        return f"The vehicle speed {self.speed}"


class VehicleWithoutEngine(Vehicle):

    def start_moving(self):
        raise NotImplemented


class VehicleWithEngine(Vehicle):

    def engine(self):
        pass

    def start_engine(self):
        self.engine()


class Car(VehicleWithEngine):

    def start_engine(self):
        pass


class Bicycle(VehicleWithoutEngine):

    def start_moving(self):
        pass
