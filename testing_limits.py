

def euro_currency(amount):
    try:
        if float(amount) > 0:
            euro = amount * .9
            return round(euro, 2)
    except ValueError:
        if str(amount).isalpha():
            return "That's not a valid currency amount"
        elif len(str(amount)) == 0:
            return "That's not a valid currency amount"


def usd_currency(amount):
    try:
        if float(amount) > 0:
            usd = amount / .9
            return round(usd, 2)
    except ValueError:
        if str(amount).isalpha():
            return "That's not a valid currency amount"
        elif len(str(amount)) == 0:
            return "That's not a valid currency amount"


def multiple_currency_euro(euro_list):
    try:
        return [round((amount * .9), 2) for amount in euro_list]
    except TypeError:
        return "That's not a valid currency amount"


def multiple_currency_usd(usd_list):
    try:
        return [round((amount / .9), 2) for amount in usd_list]
    except TypeError:
        return "That's not a valid currency amount"
    