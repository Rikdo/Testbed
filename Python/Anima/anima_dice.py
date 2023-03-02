''' Anima Dice Roller by Dash
rolls d100s by anima rules, and gives results'''

from random import *


def ROLL(d):
    return randint(1, d)

def roll_dice(base, high, open_roll):
    roll = ROLL(100)
    total = roll + base
    print('roll:' + str(roll))
    if roll <= 3 and open_roll == False:
        print('Fumble!!!')
        return -(ROLL(100)+(-30 + (roll*15)))
    elif roll >= high:
        print('Open Roll!!!')
        return roll_dice(total, high + 1, True)
    else:
        return total
        

def roll(base):
    return base + roll_dice(0, 90, False)


print('total:' +str(roll(0)))

