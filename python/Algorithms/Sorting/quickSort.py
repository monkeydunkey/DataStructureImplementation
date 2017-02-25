def quick_sort(arr, up = 0, low = None):
    low = low if low is not None else len(arr) - 1
    if (low <= up):
        return arr
    pivot = (up+low)/2
    arr[low], arr[pivot] = arr[pivot], arr[low]
    i, j = up, low-1
    pivot = arr[low]
    flag_1, flag_2 = False, False
    while j >= i:
        if arr[j] > pivot:
            j = j - 1
        else:
            flag_1 = True
        if arr[i] < pivot:
            i = i + 1
        else:
            flag_2 = True

        if flag_1 & flag_2:
            arr[j], arr[i] = arr[i], arr[j]
            j -= 1
            i += 1
    arr[j+1], arr[low] = arr[low], arr[j+1]
    arr = quick_sort(arr,up, j)
    arr = quick_sort(arr,j+2, low)
    return arr
