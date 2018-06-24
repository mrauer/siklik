import statistics

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


# Call one stock, and get a list of closing value.
def get_single_stock(stock_name):
    endpoint = 'https://api.iextrading.com/1.0/stock/'
    r = requests.get(''.join([endpoint, stock_name, '/chart/5y']))
    datapoints = r.json()

    stock_list = list()
    for datapoint in datapoints:
        stock_list.append([datapoint['close'], datapoint['date']])
    return sorted(stock_list, reverse=True, key=lambda x: x[1])


# Compute the cycles.
def compute_cycles(stock_list):
    cycles_dict = dict()
    for j in xrange(1, len(stock_list)):
        variations = list()
        has_negative = False
        for i in xrange(0, len(stock_list) - 1, j):
            try:
                original = float(stock_list[i+j][0])
                new = float(stock_list[i][0])
                # Measure the variation between 2 values.
                variation = compute_variations(original, new)
                # Continuous check.
                if variation < 0:
                    has_negative = True
                variations.append(variation)
            except:
                break
        if not has_negative and len(variations) > 1:
            cycles_dict[j] = [len(variations), statistics.mean(variations)]
    return cycles_dict


# Compute variations between two values.
def compute_variations(original_value, new_value):
    return 100 * ((new_value - original_value) / original_value)
