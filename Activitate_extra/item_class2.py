class Item:
    pay_rate = 0.8
    list = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        # Run validations to the received args
        assert price >= 0, f'Price {price} is not greater than zero!'
        assert quantity >= 0, f'Price {quantity} is not greater than zero!'

        # Assign to self obj
        self.name = name
        self.price = price
        self.quantity = quantity
        # Actions to execute
        Item.list.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)

print(Item.list)
