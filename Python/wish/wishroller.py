# In which we attempt to automate Wish Chaos Burst Rolls


#Init
from os import system #Import System for clear screen function
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#IE: print(color.BOLD + 'Hello World !' + color.END)



system('cls') # Clear Screen
print('Loading...')
LIST = open("wishlist.txt", "r") #Load list of possible side effects
ROLLS = open("wishrolls.txt", "r") #load list of rolls a player made to check against the wishlist
print('Reading...')
List = LIST.readlines() # Convert wishlist to a python list, which can then be indexed line by line




print("Welcome to WishRoller...")

for x in ROLLS:
	y = int(x)
	r = int(str(x)[::-1])
	u = int(x)+1
	d = int(x)-1
	ru = int(str(x)[::-1])+1
	rd = int(str(x)[::-1])-1
	print(color.BOLD+List[y]+color.END+"     UP: "+List[u]+"     DN: "+List[d]+"     RE: "+List[r]+"     RU: "+List[ru]+"     RD: "+List[rd])

LIST.close()
ROLLS.close()