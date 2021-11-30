import os
from utils.Strategy import Trend
path = './utils/Strategy/'
folders = os.listdir(path)

print([x[:-3] for x in folders])

option = [prop for prop in dir(Trend) if '_Strategy' in prop]
print(option)