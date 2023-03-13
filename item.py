import csv

class Item:
    pay_rate = 0.8 #Pay Rate after 20% discount(class attribute)
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # print(f"Item {name} created successfully")
        self.__name = name
        self.__price = price
        self.quantity = quantity

        self.all.append(self)

    @property
    # Property decorator = Read Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    def calculate_total_price(self):
        total_price = self.__price * self.quantity
        print(f"Total price of {self.name} is {total_price}")

    def calculate_discounted_price(self):
        self.__price = self.__price * self.pay_rate
        return self.__price

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                item.get('name'),
                float(item.get('price')),
                int(item.get('quantity'))
            )

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

