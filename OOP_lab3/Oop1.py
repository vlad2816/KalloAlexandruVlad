from random import shuffle
from typing import List


CARD_SYMBOLS = ['♠', '♥', '♦', '♣']
CARD_VALUE_MAP = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'A': 11,
    'J': 12,
    'Q': 13,
    'K': 14
}


class Card:

    def __init__(self, number: str, symbol: str):

        if number not in CARD_VALUE_MAP:
            raise ValueError('Number nu face parte din lista de numere')
        if symbol not in CARD_SYMBOLS:
            raise ValueError('Invalid card symbol.')

        self.__symbol = symbol
        self.__number = number

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self) -> str:
        # apelat cand dam print pe un obiect REturn string
        return f'<{self.__number} {self.__symbol}>'

    def __repr__(self) -> str:
        return self.__str__()  # vrem sa vedem object in interpretor Return string

    def get_value(self) -> int:
        return CARD_VALUE_MAP[self.__number]

    def __lt__(self, other) -> int:
        return self.get_value() < other.get_number()

    def __le__(self, other) -> int:
        return self.get_value() <= other.get_number()

    def __gt__(self, other) -> int:
        return self.get_value() > other.get_number()

    def __ge__(self, other) -> int:
        return self.get_value() >= other.get_number()

    def __add__(self, other) -> int:
        # return acelasi tip, dar un obiect nou.
        return self.get_value() + other.get_number()

    def __eq__(self, other) -> int:  # operator overloading
        # Returneaza boolean
        # if self.number == other.number:
        #     if self.symbol == other.symbol:
        #         return True
        # return False
        # and self.__symbol == other.get_symbol()
        return self.get_value() == other.get_number()

    # def __del__(self):
    #     """Destructor"""
    #     print('The card was deleted from the memory')


class Deck:
    """
    When calling len() on this you will get the number of cards remaining in deck.
    """

    def __init__(self) -> None:
        self.__cards = []

        for i in CARD_SYMBOLS:
            for number in CARD_VALUE_MAP:
                # card(valorile din for) cream un object
                self.__cards.append((Card(number, i)))

    def __len__(self):  # return int sau float
        return len(self.__cards)

    def get_cards(self, n) -> List[Card]:
        """Return n cards."""
        my_cards = []
        if n > len(self.__cards):
            raise ValueError('Cards cant be popped ')
        for i in range(n):
            my_cards.append(self.__cards.pop())
        return my_cards

    def shuffle(self):
        shuffle(self.__cards)
        return self.__cards


# d1 = Deck()
# print(d1.get_cards(2))
# d1.shuffle()
# print(d1.get_cards(2))
# c1 = Card('2', CARD_SYMBOLS[0])
# c2 = Card('2', CARD_SYMBOLS[1])
# # print(c1 == c2)


# print(f'Carti in pachet: {len(d1)}')
