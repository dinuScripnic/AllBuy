from requests import *
# United States Dollar - USD
# Euro - EUR
# Pound Sterling - GBP
# Swiss Franc - CHF
# Japanese Yen - JPY


def usd(amount):
    usd = amount
    rate = get('https://v6.exchangerate-api.com/v6/5fc93466e50928ba17789754/latest/USD').json()['conversion_rates']
    eur = amount * rate['EUR']
    gbp = amount * rate['GBP']
    chf = amount * rate['CHF']
    jpy = amount * rate['JPY']
    return usd, eur, gbp, chf, jpy


def eur(amount):
    eur = amount
    rate = get('https://v6.exchangerate-api.com/v6/5fc93466e50928ba17789754/latest/EUR').json()['conversion_rates']
    usd = amount * rate['USD']
    gbp = amount * rate['GBP']
    chf = amount * rate['CHF']
    jpy = amount * rate['JPY']
    return usd, eur, gbp, chf, jpy


def gbp(amount):
    gbp = amount
    rate = get('https://v6.exchangerate-api.com/v6/5fc93466e50928ba17789754/latest/GBP').json()['conversion_rates']
    usd = amount * rate['USD']
    eur = amount * rate['EUR']
    chf = amount * rate['CHF']
    jpy = amount * rate['JPY']
    return usd, eur, gbp, chf, jpy


def chf(amount):
    chf = amount
    rate = get('https://v6.exchangerate-api.com/v6/5fc93466e50928ba17789754/latest/CHF').json()['conversion_rates']
    usd = amount * rate['USD']
    eur = amount * rate['EUR']
    gbp = amount * rate['GBP']
    jpy = amount * rate['JPY']
    return usd, eur, gbp, chf, jpy


def jpy(amount):
    jpy = amount
    rate = get('https://v6.exchangerate-api.com/v6/5fc93466e50928ba17789754/latest/JPY').json()['conversion_rates']
    usd = amount * rate['USD']
    eur = amount * rate['EUR']
    gbp = amount * rate['GBP']
    chf = amount * rate['CHF']
    return usd, eur, gbp, chf, jpy
