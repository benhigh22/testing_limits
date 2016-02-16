import unittest

from testing_limits import euro_currency, multiple_currency_euro, usd_currency, multiple_currency_usd


class SingleEuroTestCase(unittest.TestCase):

    def test_currency_changes_for_one_number_to_euro(self):
        self.assertEqual(euro_currency(1), .9)

    def test_currency_changes_for_one_number_to_usd(self):
        self.assertEqual(usd_currency(.9), 1)

    def test_currency_changes_for_a_number_that_has_a_decimal_to_only_2_places_to_euro(self):
        self.assertEqual(euro_currency(.96), .86)

    def test_currency_changes_for_a_number_that_has_a_decimal_to_only_2_places_to_usd(self):
        self.assertEqual(usd_currency(.86), .96)

class MultipleEuroTestCase(unittest.TestCase):

    def test_currency_changes_for_several_numbers_returns_list_in_euros(self):
        self.assertEqual(multiple_currency_euro([1, 2, 3]), [.9, 1.8, 2.7])

    def test_currency_changes_for_several_numbers_returns_list_in_usd(self):
        self.assertEqual(multiple_currency_usd([.9, 1.8, 2.7]), [1, 2, 3])

    def test_currency_changes_for_several_numbers_returns_list_in_euros_with_decimals(self):
        self.assertEqual(multiple_currency_euro([1.2, 190.75, 4.67]), [1.08, 171.68, 4.20])

    def test_currency_changes_for_several_numbers_returns_list_in_usd_with_decimals(self):
        self.assertEqual(multiple_currency_usd([5.46, 10.23]), [6.07, 11.37])
