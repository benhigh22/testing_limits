import unittest

from testing_limits import multiple_currency_usd, multiple_currency_euro, euro_currency, usd_currency


class SingleEuroTestCase(unittest.TestCase):

    def test_currency_changes_for_one_number_to_euro(self):
        self.assertEqual(euro_currency(1), .9)

    def test_currency_changes_for_one_number_to_usd(self):
        self.assertEqual(usd_currency(.9), 1)

    def test_currency_changes_for_a_number_that_has_a_decimal_to_only_2_places_to_euro(self):
        self.assertEqual(euro_currency(.96), .86)

    def test_currency_changes_for_a_number_that_has_a_decimal_to_only_2_places_to_usd(self):
        self.assertEqual(usd_currency(.86), .96)

    def euro_test_currency_amount_is_negative(self):
        self.assertEqual(euro_currency(-10), -9)

    def usd_test_currency_amount_is_negative(self):
        self.assertEqual(euro_currency(-1), -.9)

    def euro_test_if_not_an_integer(self):
        self.assertEqual(euro_currency("a"), "That's not a valid currency amount")

    def euro_test_if_amount_has_any_characters(self):
        self.assertEqual(euro_currency(""), "That's not a valid currency amount")

    def usd_test_if_not_an_integer(self):
        self.assertEqual(usd_currency("a"), "That's not a valid currency amount")

    def usd_test_if_amount_has_any_characters(self):
        self.assertEqual(usd_currency(""), "That's not a valid currency amount")


class MultipleEuroTestCase(unittest.TestCase):

    def test_currency_changes_for_several_numbers_returns_list_in_euros(self):
        self.assertEqual(multiple_currency_euro([1, 2, 3]), [.9, 1.8, 2.7])

    def test_currency_changes_for_several_numbers_returns_list_in_usd(self):
        self.assertEqual(multiple_currency_usd([.9, 1.8, 2.7]), [1, 2, 3])

    def test_currency_changes_for_several_numbers_returns_list_in_euros_with_decimals(self):
        self.assertEqual(multiple_currency_euro([1.2, 190.75, 4.67]), [1.08, 171.68, 4.20])

    def test_currency_changes_for_several_numbers_returns_list_in_usd_with_decimals(self):
        self.assertEqual(multiple_currency_usd([5.46, 10.23]), [6.07, 11.37])

    def euro_test_currency_changes_for_several_numbers_with_letters(self):
        self.assertEqual(multiple_currency_euro([1, 2, "a"]), "That's not a valid currency amount")

    def usd_test_currency_changes_for_several_numbers_with_letters(self):
        self.assertEqual(multiple_currency_usd([1, 2, "a"]), "That's not a valid currency amount")

