a = [ 1,   2,   3,   4,   2,   1,   3,   4,   5,   6,   5,   4,   3,   2]
b = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']

dict = {}

for i, symbol in enumerate(b):
    print(i, ' ', symbol)
    dict[symbol] = dict.get(symbol, 0) + a[i]

print(dict)