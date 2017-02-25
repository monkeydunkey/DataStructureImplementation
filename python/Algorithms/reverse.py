def reverseWord(st):
    li = list(st)
    top, bottom = 0, len(li) - 1
    while(top < bottom):
        li[top], li[bottom] = li[bottom], li[top]
        top += 1
        bottom -= 1
    return "".join(li)

def reverseWords(st):
    lisOfWords = st.split(' ')
    outStr = ""
    for i in range(len(lisOfWords) - 1, -1, -1):
        outStr += " " + lisOfWords[i]
    return outStr.strip()

if __name__ == '__main__':
    print reverseWords('find you will pain only go you recordings security the into if')
    
