'''Cipher.py by Old Man Rikdo
test base for encrypting text files'''

'''def cipher_file_lines(Filename, line):
    File = open(Filename)
    Line = File.readline(line)
    print(Line)

def cipher_file(Filename):
    return cipher_file_lines(Filename, 2)


def cipher_line(Line):
    return cipher_file_lines('words.txt', Line)'''
import Tkinter

def openfile():
    file = open('words.txt')
    for line in file:
        for ch in line.strip():
            print(ord(ch))
    return

def tests():
    img = open('B.jpg')
    img.show()
    return

def cipher(givenString):
    retString = ""
    for letter in givenString:
        if letter.isalpha(): #skip non a-z characters
            if letter == 'z':
                retString += 'a'
            elif letter == 'Z':
                retString += 'A'
            else:
                retString += chr(ord(letter)+1)
        else:
            retString += letter
    return retString

def unitest():
    car = 100
    retstr = ''
    while car <= 200:
        retstr += chr(car)
        car += 1
    return retstr
        

'''print(cipher("hello?"))'''
print(unitest())
