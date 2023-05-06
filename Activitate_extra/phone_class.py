
class Item:
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity: int) -> None:
        # Run validations to the received args
        assert price >= 0, f'Price {price} is not greater than zero!'
        assert quantity >= 0, f'Price {quantity} is not greater than zero!'

        # Assign to self obj
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate


object1 = Item('Phone', 3000, 2)
object2 = Item('Laptop', 20, 3)
# the method is called by the object.
print(object1.calculate_total_price())
print(object2.calculate_total_price())
obj3 = Item('Watch', 20, 1)
obj3.apply_discount()
print(obj3.price)

# print(Item.pay_rate)  # Calling the global var of the class
