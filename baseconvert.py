from collections import deque
from math import *


class WrongInputError(Exception):
    def __init__(self, message):
        self.message = message



def hexconvert(x):
    if x in 'aA':
        return 10
    elif x in 'bB':
        return 11
    elif x in 'cC':
        return 12
    elif x in 'dD':
        return 13
    elif x in 'eE':
        return 14
    elif x in 'fF':
        return 15
def hexconvert2(x):
    if x == 10:
        return 'A'
    elif x == 11:
        return 'B'
    elif x == 12:
        return 'C'
    elif x == 13:
        return 'D'
    elif x == 14:
        return 'E'
    elif x == 15:
        return 'F'


def decimaltobase(value='', base=0):
    d = list()
    hex = list()
    bhex = bool()
    for i in range(len(value)):
        try:
            if value[i] not in "0123456789":
                # print('True')
                raise WrongInputError('Error converting non int to int')
        except TypeError:
            pass


    value = value.replace(' ', '')
    
    value = int(value)
    x = value
    for i in range(value):
        if x == 0:
            break
        else:
            code = x%base
            if code > 9 and code <16 :
                hex.append(code)
            x /= base
            x = floor(x)
            d.insert(0, code)
    for a in range(len(d)):
        if d[a] in hex:
            d[a] = hexconvert2(d[a])
    result = ''
    for index in range(len(d)):
        result += str(d[index])
    return result
    


def basetodecimal(value='', base=0):
    hex = list()
    bhex = bool()
    try:
        for i in range(len(value)):
                if value[i] not in "0123456789abcdefABCDEF":
                    print('True')
                    raise WrongInputError('Error converting non int to int')
    except TypeError as e:
        print('Error', e)
    except WrongInputError as e:
        print('Error', e.message)
    for i in range(len(value)):
        if value[i] in 'abcdefABCDEF':
            bhex = True
            hex.append(value[i])
        else: continue

    value = value.replace(' ', '')
    d = list(value)
    powdata = len(d) - 1
    numdata = 0
    for x in range(len(d)):
        if bhex and d[x] in hex:
            d[x] = hexconvert(d[x])
        basepower = pow(base, powdata)
        numdata += int(d[x])*basepower
        powdata -= 1
        
    result = str(numdata)
    # returns result
    return result