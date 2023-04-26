from Oop1 import Card, Deck


def septica(deck: Deck):
    for card in deck:
        if card.get_value() >= 7:
            yield card


d1 = Deck()
# d1.shuffle()
# x_cards = d1.get_cards(2)

# print(sum(x_cards))

d1_iter = iter(d1)


print(next(d1_iter))
print(next(d1_iter))
print('*' * 40)

septica_card = septica(d1)

for i in septica_card:
    print(i)
