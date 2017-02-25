# this is a dynamic programming implementation of Edit distance or the smallest change required to covert one string to the other one

def calc_editDistance(str1, str2):
    arr = [[0 for x in xrange(len(str1) + 1)] for y in xrange(len(str2) + 1) ]
    for i in xrange(len(str1) + 1):
        arr[0][i] = i
    for i in xrange(len(str2) + 1):
        arr[i][0] = i
    for i in xrange(len(str2)):
        for j in xrange(len(str1)):
            diff = 1 if str1[j] != str2[i] else 0
            arr[i+1][j+1] = min(1 + arr[i][j+1], 1 + arr[i+1][j], diff + arr[i][j])

    return arr[len(str2)][len(str1)]


if __name__ == '__main__':
    print calc_editDistance('suny', 'sny')
