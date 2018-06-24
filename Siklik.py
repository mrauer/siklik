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


# Call one stock, and get a dict of closing value.
def get_single_stock(stock_name):
    endpoint = 'https://api.iextrading.com/1.0/stock/'
    r = requests.get(''.join([endpoint, stock_name, '/chart/5y']))
    datapoints = r.json()

    stock_dict = dict()
    for datapoint in datapoints:
        stock_dict[datapoint['date']] = datapoint['close']
    return stock_dict
