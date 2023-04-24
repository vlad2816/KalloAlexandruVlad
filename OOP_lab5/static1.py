class UserAccount:

    def __init__(self, email) -> None:
        self.email = email
        self.__favorites_products = []

    @property
    def favorites(self):
        return self.__favorites_products

    def add_fav(self, product):
        self.__favorites_products.append(product)


class Product:

    count = 0  # Atribut de clasa / atribut static

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        Product.count += 1

    def add_to_favorites(self, user_account):
        user_account.add_fav(self)

    def __str__(self) -> str:
        return f'<Product name: {self.name}>'

    def __repr__(self) -> str:
        return self.__str__()


if __name__ == '__main__':  # Main guard
    user1 = UserAccount('vlad@yahoo.com')
    prod1 = [Product('Ulei de masline', 45), Product('Ceapa', 3)]

    prod1[-1].add_to_favorites(user1)
    print(user1.__favorites_products)
    print(Product.count)  # asa accesez atributul static count.
