

def euro_currency(value):
    euro = value * .9
    return round(euro, 2)

def usd_currency(value):
    usd = value / .9
    return round(usd, 2)

def multiple_currency_euro(euro_list):
    return [round((amount * .9), 2) for amount in euro_list]

def multiple_currency_usd(usd_list):
    return [round((amount / .9), 2) for amount in usd_list]