def insertion_sort(arr):
    for i in range(1, len(arr)):
        ele = arr[i]
        j = i
        while j > 0:
            if arr[j-1] > ele:
                arr[j] = arr[j-1]
                j -= 1
            else:
                break
        arr[j] = ele
    return arr
                
