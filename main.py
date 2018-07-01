import json
import sys

import siklik

if sys.argv > 1:
    args = json.loads(sys.argv[1])
    # Update the list of stocks.
    if 'action' in args and args['action'] == 'update':
        num_symbols = siklik.get_symbols()
        print ' '.join([str(num_symbols), 'symbols have been processed'])

    # Perform the core process.
    if 'action' in args and args['action'] == 'run':
        symbols = siklik.get_stock_list()
        # Iterate on each individual stock.
        for symbol in symbols:
            try:
                stock_dict = siklik.get_single_stock(symbol)
            except Exception, e:
                print e
                pass
            # Compute the cycles.
            cycles_dict = siklik.compute_cycles(stock_dict)

            # Eventually use clustering in 3D.
            for key, values in cycles_dict.iteritems():
                print str(key) + str(values)
                siklik.write_to_file(values)
                # Will only keep the highest cycle found.
                break
