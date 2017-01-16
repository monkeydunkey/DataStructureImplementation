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

    return pre_suff
