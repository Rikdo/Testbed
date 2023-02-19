'''Anima Combat Calculator by Dash McLughlin
Takes a base attack, attack type, Base damage
Defender AT, base defense, and calculates damage

v0.1 base attack/defense difference to percentage'''

from random import *

def round_down(num):
    #print(num)
    if num == int(num):
        return int(num)
    else:
        return round_down(round(num-0.10, 1))

def ROLL(d):
    '''Rolls one d___ where the input is the side number'''
    return randint(1, d)

def roll_dice(base, high, open_roll):
    roll = ROLL(100)
    total = roll + base
    print('roll:' + str(roll))
    if roll <= 3 and open_roll == False:
        fumble = -(ROLL(100)+(-30 + (roll*15)))
        print('Fumble!!! '+str(fumble))
        return fumble
    elif roll >= high:
        print('Open Roll!!!')
        return roll_dice(total, high + 1, True)
    else:
        return total

def roll(base):
    '''Returns the base stat, plus the results of a d100'''
    return base + roll_dice(0, 90, False)


def get_diff(ATT, DEF, Roll):
    if Roll == 'roll':
        print('ATT roll:')
        att_roll = roll(ATT)
        print('DEF roll:')
        def_roll = roll(DEF)
    else:
        att_roll = ATT
        def_roll = DEF
    print('Final ATT: '+str(att_roll))
    print('Final DEF: '+str(def_roll))
    diff = att_roll - def_roll
    return diff
        
def diff_to_range(diff):
    '''finds the range of the diffrence between att and def'''
    base = round((diff / 10.0), 1)
    '''positives round up, negetives round down'''
    if diff > 0:
        rng = int(base)
    elif diff < 0:
        rng = round_down(base)
    else:
        rng = 0
    return rng

def get_counter(rng):
    counter = (abs(rng) - 1) * 5
    return ('+')+str(counter)+(' C')

def get_percent(rng, AT):
    if rng <= 2:
        percent = 0
    elif rng == 4:
        percent = (rng - AT - 1) * 10
    elif rng >= 5:
        percent = (rng - AT) * 10
    elif rng == 3 and AT <= 2:
        percent = 10
    else:
        percent = 0
    if percent <= 0:
        percent = 0
    return percent

def get_results(ATT, DEF, DMG, AT, Roll):
    diff = get_diff(ATT, DEF, Roll)
    print('Diffrence: '+str(diff))
    rng = diff_to_range(diff)
    if rng < 0:
        print('Attack Countered! '+str(get_counter(rng)))
    else:
        percent = get_percent(rng, AT)
        print('Damage %: '+str(percent)+'%')
        damage = round(DMG*(percent/100.00))
        print('Final Damage: '+str(damage))

def combat_calc(Roll):
    ATT = 131#int(input('Attack: '))
    DEF = 56#int(input('Dodge: '))
    DMG = 30#int(input('Damage: '))
    AT = 0#int(input('AT: '))
    get_results(ATT, DEF, DMG, AT, Roll)
    
        
def tests():
    '''print(round_down(13))
    print(round_down(13.4))
    print(round_down(-13.4))
    print(diff_to_range(13))
    print(diff_to_range(-13))
    print(diff_to_range(20))
    print(diff_to_range(135))
    print(get_counter(4))'''
    '''print(get_results(-134, 1))'''
    combat_calc('rol')

tests()
input()
