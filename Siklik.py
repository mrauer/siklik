import requests


# Get symbols and overwrite file.
def get_symbols():
    r = requests.get('https://api.iextrading.com/1.0/ref-data/symbols')
    symbols = r.json()
    f = open('./data/symbols.dat', 'w')
    for symbol in symbols:
        if symbol['isEnabled']:
            f.write(','.join([symbol['name'], symbol['symbol']]) + '\n')
    f.close()
    return len(symbols)
