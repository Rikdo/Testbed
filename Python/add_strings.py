# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.

num1 = '364'
num2 = '1836'

def solution1(n1, n2):
    return eval(n1 + "+" + n2)                  #Combines the strings and operator into a single line and evaluates it as code

def solution2(n1, n2):
    u1, u2 = 0, 0
    m1, m2 = 10**(len(n1)-1), 10**(len(n2)-1)   #indexes the starting place of the number, ie: 10's, 100's, 1000's etc

    for i in n1:
        u1 += (ord(i) - ord("0")) * m1          #Gets the digit by comparing unicode character to 0, multiplying by m1 places
        m1 = m1//10                             #Shifts the places index 1 digit down for the next loop

    for i in n2:
        u1 += (ord(i) - ord("0")) * m2
        m2 = m2//10
        
    return str(u1+u2)

print(solution1(num1, num2))
print(solution2(num1, num2))

# def unicode_test(n1):
#     for i in n1:
#         print(ord(i))
# unicode_test(num1)