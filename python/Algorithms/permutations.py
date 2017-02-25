def recurPermute(alphaDict, st):
    returnSet = set()
    flag = False
    for x in alphaDict.iterkeys():
        if alphaDict[x] != 0:
            flag = True
            break
    if not flag:
        return set([st])
    for x in alphaDict.iterkeys():
        if alphaDict[x] == 0:
            continue
        alphaDict[x] -= 1
        setR = recurPermute(alphaDict, st + x)
        alphaDict[x] += 1
        returnSet = returnSet.union(setR)
    return returnSet

def getPermutations(st):
    alphaDict = {}
    for x in st:
        alphaDict[x] = alphaDict.get(x, 0) + 1
    returnSet = recurPermute(alphaDict, "")
    return returnSet

if __name__ == '__main__':
    output = getPermutations("abcd")
    print output, len(output)
