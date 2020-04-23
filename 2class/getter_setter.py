class BadPractice:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


class GoodPractice:

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


badPractice = BadPractice(2.00)
print(badPractice.get_price())
badPractice.set_price(3.00)
print(badPractice.get_price())


goodPractice = GoodPractice(2.00)
print(goodPractice.price)
goodPractice.price = 3.00
print(goodPractice.price)
