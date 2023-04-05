from Oop1 import Card, Deck

d1 = Deck()
d1.shuffle()
x_cards = d1.get_cards(2)

print(sum(x_cards))
