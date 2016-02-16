

def euro_currency(amount):
    euro = amount * .9
    return round(euro, 2)

def usd_currency(amount):
    usd = amount / .9
    return round(usd, 2)

def amt_not_valid(amount):
    if amount.isalpha():
        return "That's not a valid currency amount"

def amt_no_chars(amount):
    if len(amount) == 0:
        return "That's not a valid currency amount"

def multiple_currency_euro(euro_list):
    return [round((amount * .9), 2) for amount in euro_list]

def multiple_currency_usd(usd_list):
    return [round((amount / .9), 2) for amount in usd_list]

