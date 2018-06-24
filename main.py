import json
import sys

import Siklik

if sys.argv > 1:
    args = json.loads(sys.argv[1])
    if 'action' in args and args['action'] == 'update':
        num_symbols = Siklik.get_symbols()
        print ' '.join([str(num_symbols), 'symbols have been processed'])

    if 'action' in args and args['action'] == 'run':
        print Siklik.get_single_stock('fb')
