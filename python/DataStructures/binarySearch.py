def binary_search(arr, key):
    hi = len(arr)
    lo = 1
    while hi >= lo:
        ind = hi - ((hi - lo)/2) - 1
        if arr[ind] < key:
            lo = ind + 2
        elif arr[ind] > key:
            hi = ind
        else:
            return arr[ind]

    return False




