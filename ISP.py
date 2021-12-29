"""
Interface Segregation Principle

Actually, This principle suggests that “A client should not be forced to implement an interface that it does not use”.
"""


class Shape:

    def draw_circle(self):
        raise NotImplemented

    def draw_square(self):
        raise NotImplemented


class Circle(Shape):

    def draw_circle(self):
        pass

    def draw_square(self):
        pass


"""In the above example, we need to call an unnecessary method in the Circle class.
Hence the example violated the Interface Segregation Principle.
"""


class Shape:

    def draw(self):
        raise NotImplemented


class Circle(Shape):

    def draw(self):
        pass


class Square(Shape):

    def draw(self):
        pass
