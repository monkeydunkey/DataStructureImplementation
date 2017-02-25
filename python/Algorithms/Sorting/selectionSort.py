def selection_sort(arr):
    for i in range(len(arr)):
        min_ = None
        min_index = None
        for j in range(i, len(arr)):
            if (min_ is None) | (min_ > arr[j]):
                min_ = arr[j]
                min_index = j
        arr[i], arr[min_index] = min_, arr[i]
    return arr
