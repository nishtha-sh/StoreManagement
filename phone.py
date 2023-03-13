from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes and methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than equal to zero"

        # Assign to self object
        self.broken_phones = broken_phones

# phone1 = Phone('samsung', 1000, 2, 1)