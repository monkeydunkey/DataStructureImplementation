def calc_lcs(str1, str2):
    arr = [ [0 for x in range(len(str1) +1)] for h in range(len(str2) + 1)]
    for i in range(len(str2)):
        for j in range(len(str1)):
            if str1[j] == str2[i]:
                arr[i+1][j+1] = arr[i][j] + 1
            else:
                arr[i+1][j+1] = max(arr[i][j+1], arr[i+1][j])
    return arr

if __name__ == '__main__':
    print calc_lcs('abcdaf', 'acbcf')
