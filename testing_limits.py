
class Money:

    def __init__(self, amount=0, currency=None):
        self.amount = amount
        self.currency = currency

    def euro_currency(self, amount):
        euro = amount * .9
        return round(euro, 2)

    def usd_currency(self, amount):
        usd = amount / .9
        return round(usd, 2)

    def amt_not_valid(self, amount):
        if amount.isalpha():
            return "That's not a valid currency amount"

    def amt_no_chars(self, amount):
        if len(amount) == 0:
            return "That's not a valid currency amount"

    def multiple_currency_euro(self, euro_list):
        return [round((amount * .9), 2) for amount in euro_list]

    def multiple_currency_usd(self, usd_list):
        return [round((amount / .9), 2) for amount in usd_list]

