def getIndex(arr, val, top, bottom):
    if top >= bottom:
        if arr[top] > val:
            return top
        else:
            return top + 1
      
    ind = (top + bottom) // 2
    if arr[ind] > val:
        return getIndex(arr, val, top, ind - 1)
    else:
        return getIndex(arr, val, ind + 1, bottom)


def highest_product(arr, k):
    cand = sorted(arr[:k])
    for i in range(k, len(arr)):
        ind = getIndex(cand, arr[i], 0, len(cand) - 1)
        if ind > 0:
            cand.insert(ind, arr[i])
            del cand[0]

    print cand
    mult = 1
    for ca in cand:
        mult *= ca
    print mult

if __name__ == '__main__':
    arr = [2,4,5,0,1,3,7]
    highest_product(arr, 4)
