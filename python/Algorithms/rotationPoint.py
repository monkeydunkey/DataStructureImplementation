def getRot(arr, top, bottom):
    if top >= bottom:
        return 0
    ind = (top + bottom) // 2
    if arr[ind] < arr[ind - 1]:
        return ind
    elif arr[ind] > arr[ind + 1]:
        return ind + 1
    else:
        if arr[ind] > arr[0]:
            return getRot(arr, ind + 1, bottom)
        else:
            return getRot(arr, top, ind - 1)

if __name__ == '__main__':
    arr = ['ptolemaic','retrograde','supplant','undulate',
    'apple','asymptote','babka','banoffee','engender','karpatka','othellolagkage']
    print getRot(arr, 0, len(arr) - 1)


