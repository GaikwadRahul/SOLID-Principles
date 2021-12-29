"""
The Dependency Inversion Principle (DIP)

“Abstractions should not depend on details. Details should depend on abstraction.
High-level modules should not depend on low-level modules. Both should depend on abstractions”
"""


class NewsPerson:

    @staticmethod
    def publish(news: str) -> None:
        print(NewsPaper().publish(news=news))


class NewsPaper:

    @staticmethod
    def publish(news: str) -> None:
        print(f"{news} Hello newspaper")


person = NewsPerson()
print(person.publish("News Paper"))

"""
The project class is a high-level module and backend & frontend are the low-level modules. In this example, 
we found that the high-level module depends on the low-level module. Hence this example are violated the 
Dependency Inversion Principle.
"""


class NewsPerson:

    @staticmethod
    def publish(news: str, publisher=None) -> None:
        print(publisher.publish(news=news))


class NewsPaper:

    @staticmethod
    def publish(news: str) -> None:
        print("{} news paper".format(news))


class Facebook:

    @staticmethod
    def publish(news: str) -> None:
        print(f"{news} - share this post on {news}")


person = NewsPerson()
person.publish("hello", NewsPaper())
person.publish("facebook", Facebook())
