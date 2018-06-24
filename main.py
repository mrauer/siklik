import json
import sys

import Siklik

if sys.argv > 1:
    args = json.loads(sys.argv[1])
    if 'action' in args and args['action'] == 'update':
        num_symbols = Siklik.get_symbols()
        print ' '.join([str(num_symbols), 'symbols have been processed'])

    if 'action' in args and args['action'] == 'run':
        stock_list = Siklik.get_single_stock('HELE')
        cycles_dict = Siklik.compute_cycles(stock_list)

        # Eventually use clustering in 3D.
        for key, value in cycles_dict.iteritems():
            print str(key) + str(value)
            break
