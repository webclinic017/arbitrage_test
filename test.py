from utils import Alpha_Function

names = [prop for prop in dir(Alpha_Function) if (prop[0] != "_" ) & (prop != 'np') & (prop != 'pd')]

print(names)
