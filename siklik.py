import statistics

import requests


def get_symbols():
    """Get symbols and overwrite input file."""
    r = requests.get('https://api.iextrading.com/1.0/ref-data/symbols')
    symbols = r.json()
    f = open('./data/symbols.dat', 'w')
    for symbol in symbols:
        if symbol['isEnabled']:
            f.write(','.join([symbol['name'], symbol['symbol']]) + '\n')
    f.close()
    return len(symbols)


def get_single_stock(stock_name):
    """Get single stock historical data from API.

    Keyword arguments:
    stock_name     --     string (name of the stock)

    Returns:
    {}             --     dict of stock information
    """
    endpoint = 'https://api.iextrading.com/1.0/stock/'
    r = requests.get(''.join([endpoint, stock_name, '/chart/5y']))
    datapoints = r.json()

    stock_list = list()
    for datapoint in datapoints:
        stock_list.append([datapoint['close'], datapoint['date']])
    return {"stock_name": stock_name,
            "stock_list": sorted(stock_list, reverse=True, key=lambda x: x[1])}


def compute_cycles(stock_dict):
    """Compute single stock cycles.

    Keyword arguments:
    stock_dict     --     dict (single stock historical data)

    Returns:
    cycles_dict    --     dict of cycles
    """
    cycles_dict = dict()
    stock_list = stock_dict['stock_list']
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
            except Exception, e:
                print e
                break
        if not has_negative and len(variations) > 1:
            cycles_dict[j] = [j, len(variations),
                              statistics.mean(variations),
                              stock_dict['stock_name']]
    return cycles_dict


def compute_variations(original_value, new_value):
    """Compute variations between two values."""
    return 100 * ((new_value - original_value) / original_value)


def get_stock_list():
    """Get the list of stocks from flat file."""
    symbols = set()
    f = open('./data/symbols.dat')
    for line in f.readlines():
        symbol = line.split(',')[1].replace('\n', '')
        symbols.add(symbol)
    return symbols


def write_to_file(values):
    """Store the computed cycles into a flat file."""
    f = open('./data/data.csv', 'a')
    f.write(''.join([','.join((str(e) for e in values)), "\n"]))
    f.close()
