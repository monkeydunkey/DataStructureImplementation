def merge(left, right):
    left_i, right_i = 0, 0
    supp = []
    while (left_i < len(left)) & (right_i < len(right)):
        if right[right_i] > left[left_i]:
            supp.append(left[left_i])
            left_i += 1
        else:
            supp.append(right[right_i])
            right_i += 1
    if left_i < len(left):
        supp.extend(left[left_i:])
    else:
        supp.extend(right[right_i:])
    return supp

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr)/2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)
