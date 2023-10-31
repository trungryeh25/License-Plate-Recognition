def normalize(text):
    lst = text.split()
    temp = ''
    for i in lst:
        temp += i

    a = list(temp)
    if (a[2] == '0'):
        a[2] = 'D'
    elif (a[2] == '1'):
        a[2] = 'T'
    elif (a[2] == '8'):
        a[2] = 'B'

    for i in range(len(a)):
        if (i != 2):
            if (a[i] == 'D'):
                a[i] = '0'
            elif (a[i] == 'T'):
                a[i] = '1'
            elif (a[i] == 'B'):
                a[i] = '8'
    return ''.join(a)