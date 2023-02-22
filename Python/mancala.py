#Mancala Calc

#DEFINING THE PITS AS BELOW
###########################
#    13 12 11 10 09 08    #
# 00                   07 #
#    01 02 03 04 05 06    #
###########################
from os import system                           
import time

keepgoing = True
RESET = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
game = RESET
moves = [0]
hand = 0
stillurturn = True
counter = 0
movelist = [3, 5, 5, 1, 1, 1, 1, 1, 1, 1]#[0, 5, 5, 6, 3, 6, 2]


def play(index):
	if sum(game[0:6]) <= 0:
		print('No more stones to play!')
		return False
	elif game[index] == 0:
		print('There are no stones in that pocket.\nTRY AGAIN\n')
		return play(index+1)
	else:
		hand = game[index]
		game[index] = 0
		while hand > 1:
			index += 1
			if index >= 14:
				index = 1
			game[index] += 1 #droping one stone
			hand -= 1
		#last stone phase
		index += 1
		if index >= 14:
			index = 1
		if index == 7:
			#you ended in the right spot, take another turn!
			game[index] += 1
			print('\nMove ended in bank.  Take another turn!')
			return True
		elif game[index] == 0:
			#you landed in an empty pit
			if game[14-index] != 0:
				game[7] += game[14-index] +1
				game[index] = 0
				game[14-index] = 0
				print('\nStones Captured! Turn Ends.')
				return False
			else:
				game[index] += 1 #droping one stone
				hand -= 1
				print('\nTurn Ends on empty pit')
				return False
		elif game[index] >= 1:
			game[index] += 1
			return play(index)
			#print('Turn continues!')
		
def printGS():
	#system('cls')
	print('\n\n###########################')
	print('#    '+str(game[13]).rjust(2)+' '+str(game[12]).rjust(2)+' '+str(game[11]).rjust(2)+' '+str(game[10]).rjust(2)+' '+str(game[9]).rjust(2)+' '+str(game[8]).rjust(2)+'    #')
	print('# '+str(game[0]).rjust(2)+'                   '+str(game[7]).rjust(2)+' #')
	print('#    '+str(game[1]).rjust(2)+' '+str(game[2]).rjust(2)+' '+str(game[3]).rjust(2)+' '+str(game[4]).rjust(2)+' '+str(game[5]).rjust(2)+' '+str(game[6]).rjust(2)+'    #')
	print('###########################')
	if moves[0] == 0:
		print('New Game!')
	else:
		print('Moves taken: '+str(moves))
	#print('Press Ctrl-C to quit.')



def nextmove(m, l):
	if l <= -1:
		return False
	elif m[l] >= 6:
			movelist[l] = 1
			return nextmove(m, l-1)
	else:
		movelist[l] += 1
		#movelist = m
		return True

def reset(L):	
	game = RESET
	moves = [0]
	hand = 0
	stillurturn = True
	counter = 0
	return nextmove(movelist, L-1)

try:
	while keepgoing:
		while stillurturn:
			#printGS()
			if movelist[counter] >= 1:
				selection = movelist[counter]
			else:
				selection = int(input('\nWhich pocket do you want to move?\n'))
			stillurturn = play(selection)
			if moves[0] == 0:
				moves[0] = selection
			else:
				moves.append(selection)
			counter += 1
		#printGS()
		print('EOT'+str(moves)+' = '+str(game[7]))
		#print('Movelist: '+str(movelist))
		keepgoing = reset(len(moves))
	print('Finished!')
except KeyboardInterrupt:
	print('\nDone.')