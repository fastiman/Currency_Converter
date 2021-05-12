import requests

currency_code_from = input().lower()
currency_code_to = input().lower()
amount = 0
cache_rate = {}


def get_exchange(code_from, code_to):
    url = f"http://www.floatrates.com/daily/{code_from}.json"
    r = requests.get(url)
    if r:
        rate = r.json()[code_to]['rate']
        cache_rate[code_to] = rate
        res = round(amount * rate, 2)
        return f"You received {res} {code_to.upper()}."
    else:
        return 'Invalid resource or currency code'


def get_base_cache():
    if currency_code_from == 'usd':
        cache_rate['usd'] = 1
        get_exchange(currency_code_from, 'eur')
    elif currency_code_from == 'eur':
        cache_rate['eur'] = 1
        get_exchange(currency_code_from, 'usd')
    else:
        get_exchange(currency_code_from, 'usd')
        get_exchange(currency_code_from, 'eur')


get_base_cache()


while currency_code_to:
    amount = float(input())
    print("Checking the cache...")
    rate_from_cache = cache_rate.get(currency_code_to)
    if rate_from_cache:
        print("Oh! It is in the cache!")
        res_from_cache = round(amount * rate_from_cache, 2)
        print(f"You received {res_from_cache} {currency_code_to.upper()}.")
    else:
        print("Sorry, but it is not in the cache!")
        print(get_exchange(currency_code_from, currency_code_to))

    currency_code_to = input().lower()
