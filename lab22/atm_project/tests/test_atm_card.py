from unittest import TestCase
from src.lib.atm import Card
from datetime import datetime


class TestConstructor(TestCase):

    def test_attributes_values(self):
        """Test that the attributes are generated correctly."""
        card = Card("test", "0837")

        self.assertIsInstance(card.number, str)
        self.assertEqual(len(card.number), 8)
        self.assertIsInstance(card.expire_date, datetime)
        self.assertIsInstance(card.security_code, int)
        self.assertGreaterEqual(card.security_code, 100)
        self.assertLessEqual(card.security_code, 1000)


class TestMethods(TestCase):

    def test_get_balance(self):
        test1 = Card('x', '1234')
        test1.get_balance()
        self.assertIsInstance(test1.get_balance, int)

    def test_add_money(self):
        test2 = Card('y', '2345')
        test2.add_money(10)

    def test_is_equal(self):
        self.assertEqual(self.test_add_money, self.test_get_balance)
