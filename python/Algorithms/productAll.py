def productAll(arr):
    zeros = []
    product  = 1
    for i, a in enumerate(arr):
        if a != 0:
            product *= a
        else:
            zeros.append(i)

    ze = len(zeros) > 1
    for i, a in enumerate(arr):
        if ze:
            arr[i] = 0
        elif a == 0:
            arr[i] = product
        elif len(zeros) == 0:
            arr[i] = product / a
        else:
            arr[i] = 0
    return arr
    
if __name__ == '__main__':
    print productAll([0, 3, 4, 0])
