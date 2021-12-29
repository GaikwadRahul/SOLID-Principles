"""
Open and Closed Principle(OCP):
Software entities (classes, function, module) open for extension, but not for modification (or closed for modification)
"""


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'normal':
            return self.price * 0.2
        elif self.customer == 'vip':
            return self.price * 0.4


"""
This example is failed to pass the Open and Close Principle(OCP). Assume, we have a super VIP customer 
and we want to give a discount of 0.8 percentage. we can’t modify the give_discount method. Only we can
extend the method.
"""


class Discount:

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):

    def get_discount(self):
        return super().get_discount() * 2


class SuperVIPDiscount(VIPDiscount):

    def get_discount(self):
        return super().get_discount() * 2
