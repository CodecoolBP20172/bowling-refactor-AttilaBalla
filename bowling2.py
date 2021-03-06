def handlechar(ch, mode='int'):
    if (mode == 'int'):
        try:
            return int(ch)
        except ValueError:
            return ch
    if (mode == 'value'):
        try:
            return int(ch)
        except ValueError:
            if (ch == '-'):
                return 0
            else:
                return 10


def handlespare(scorelist, index):
    result = 10 - scorelist[index-1] + handlechar(scorelist[index+1], 'value')
    return result


def handlestrike(scorelist, index):
    result = 10 + handlechar(scorelist[index+1], 'value')
    if (scorelist[index+2] == '/'):
        result += 10 - scorelist[index+1]
    else:
        result += handlechar(scorelist[index+2], 'value')
    return result


def score(scorestring):
    result = 0
    lastframe = False
    scorelist = [ch.upper() for ch in scorestring]  # make a list out of the input and capitalize all letters
    scorelist = list(map(handlechar, scorelist))  # convert all numbers to int from str

    for index, item in enumerate(scorelist):
        if (lastframe):
            break
        try:
            result += item
        except TypeError:
            if(item == '/'):
                if ((len(scorelist) - index-1) == 1):
                    lastframe = True
                result += handlespare(scorelist, index)
            elif(item == 'X'):
                if ((len(scorelist) - index-1) == 2):
                    lastframe = True
                result += handlestrike(scorelist, index)
    return result

print('The given scorestring has a value of', score('1/35XXX458/X3/23'))
