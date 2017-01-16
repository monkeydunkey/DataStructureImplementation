def search_kmp(string, patt):
    # This first step is to build the pattern array for prefix and suffix
    patt = list(patt)
    pre_suff = []
    i = 0
    for k, ele in enumerate(patt):
        if k == 0:
            pre_suff.append(0)
            continue
        else:
            if patt[i] == patt[k]:
                pre_suff.append(i+1)
                i = i+1
            else:
                while i > 0:
                    i = pre_suff[i-1]
                    if patt[i] == patt[k]:
                        pre_suff.append(i+1)
                        i = i+1
                        break
                if len(pre_suff) != k+1:
                    pre_suff.append(0)

    # now the prefix and suffix patterns are ready, time to do the actual
    # pattern match
    string = list(string)
    k = 0 
    matches = []
    for i, ele in enumerate(string):
        if patt[k] == ele:
            if k == len(patt) - 1:
                matches.append( {'ind': i-k, 'patt': ''.join(patt) })
                k = pre_suff[k]
                continue
            k = k + 1
        else:
            while k > 0:
                k = pre_suff[k-1]
                if patt[k] == ele:
                    k = k + 1
                    break
    return 'No match found' if len(matches) == 0 else matches

