'''searchPat.py by Dash McLaughlin
searches for given pattern in given string'''


def searchChar(c, s):
    '''checks if given string contains given character'''
    if s == '':
        return False
    else:
        if s[0] == c:
            return True
        else:
            return searchChar(c, s[1:])

def matchString(p, s):
    '''Checks if given string contains given prefix'''
    if p == '':
        return True
    elif s == '':
        return False
    else:
        if p[0] == s[0]:
            return matchString(p[1:], s[1:])
        else:
            return False

def searchString(key, s):
    if s == '':
        return False
    elif key == '':
        return True
    else:
        if s[0] == key[0]:
            if matchString(key, s) == True:
                return True
            else:
                return searchString(key, s[1:])
        else:
            return searchString(key, s[1:])
        

def matchPat(pat, s):
    if pat == '':
        return True
    elif s == '':
        return False
    elif pat[0] == '*':
        if pat[1] == s[0]:
            return matchPat(pat[1:], s[1:])
        else:
            return matchPat(pat, s[1:])
    elif pat[0] == s[0]:
        return matchPat(pat[1:], s[1:])
    else:
        return matchPat(pat, s[1:])

#def searchPat(pat, s)

def tests():
    '''if searchChar('d', 'abc') == True:
        print('true')
    else:
        print('false')
    if searchChar('b', 'abc') == True:
        print('true')
    else:
        print('false')
    if matchString('ab', 'abc') == True:
        print('true')
    else:
        print('false')
    if matchString('bc', 'abc') == True:
        print('true')
    else:
        print('false')
    if matchString('ac', 'abc') == True:
        print('true')
    else:
        print('false')
    if searchString('ac', 'abc') == True:
        print('true')
    else:
        print('false')
    if searchString('bc', 'abc') == True:
        print('true')
    else:
        print('false')'''
    if matchPat('bc', 'abc') == True:
        print('true')
    else:
        print('false')
    if matchPat('c*e*g', 'abcdefg') == True:
        print('true')
    else:
        print('false')
    if matchPat('a*c', 'abcdefg') == True:
        print('true')
    else:
        print('false')
    if matchPat('a*f*c', 'abcdefg') == True:
        print('true')
    else:
        print('false')



tests()
input()
