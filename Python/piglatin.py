'''PigLatin.py by Dash McLaughlin
translates txt file to pig latin'''



def is_vowel(letter):
    ''' cheacks if character is a vowel or not'''
    if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or letter == 'i' or letter == 'I' or letter == 'o' or letter == 'O' or letter == 'u' or letter == 'U':
        return True
    else:
        return False

def to_latin(word, tag):
    '''takes word, puts the begining constanants at end, and returns with 'a' on the end'''
    if is_vowel(word[0]) or word[0] == '':
        return word + tag +'ay'
    else:
        tag = tag + word[0]
        return to_latin(word[1:], tag)

def Translate(word):
    '''simplifies to_latin function'''
    return to_latin(word, '')

def file_to_latin(file, Line):
    fin = open(file)
    line = fin.readline(Line)
    word = line.strip()
    if word == '':
        return
    else:
        print(Translate(word))
        return file_to_latin(file, Line + 1)
        

def tests():
    '''if True == is_vowel('c'):
        print('vowel')
    else:
        print('const')
    if True == is_vowel('e'):
        print('vowel')
    else:
        print('const')
    
    print(to_latin('chello', ''))
    print(Translate('brag'))'''

    file_to_latin('words.txt', 2)
    input()

tests()
