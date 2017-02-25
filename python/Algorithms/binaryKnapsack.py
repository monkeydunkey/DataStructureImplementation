# This implementation consider that there is a limited supply of items

def calMaxVal(items, weight):
    # each element in items is a dict of the form {'weight':x, 'value':y}
    arr = [[0 for x in xrange(len(items) + 1)] for y in xrange(weight + 1)]
    for i in xrange(weight):
        for j in xrange(len(items)):
            val = arr[i + 1 - items[j]['weight']][j] + items[j]['value'] if i + 1 - items[j]['weight'] >=0 else 0
            arr[i+1][j+1] = max( val, arr[i+1][j] )
    return arr[-1][-1]

if __name__ ==  '__main__':
    items = [{'weight': 6, 'value': 30},
            {'weight': 3, 'value': 14},
            {'weight': 4, 'value': 16},
            {'weight': 2, 'value': 9}
            ]
    weight = 10
    print calMaxVal(items, weight)
