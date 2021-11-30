from utils.Strategy import Candles


methods = {'Candles': Candles.Run}

method_name = 'Candles'

if method_name in methods:
    methods[method_name]()