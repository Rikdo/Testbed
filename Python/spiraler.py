#Spirals
import pyautogui, time, math, pyperclip

def spiralIn(a, b, i):
	while distance > 0:
		pyautogui.dragRel(distance*a, distance*b, duration=0.1)   # move right
		distance = distance - i
		pyautogui.dragRel(-distance*a, distance*b, duration=0.1)   # move down
		distance = distance - i
		pyautogui.dragRel(-distance*a, -distance*b, duration=0.1)  # move left
		distance = distance - i
		pyautogui.dragRel(distance*a, -distance*b, duration=0.1)  # move up
		distance = distance - i
def spiralOut(a, b, i):
	distance = 0
	while distance < scale:
		pyautogui.dragRel(distance*a, -distance*b, duration=0.1)
		distance = distance + i
		pyautogui.dragRel(-distance*a, -distance*b, duration=0.1)
		distance = distance + i
		pyautogui.dragRel(-distance*a, distance*b, duration=0.1)
		distance = distance + i
		pyautogui.dragRel(distance*a, distance*b, duration=0.1)
		distance = distance + i

def ASpiralOut(a, b, t, i, e, c):
	#Archimedean Spiral
	#a=first leg length
	#b=how tight the coil is
	#t=time counter
	#i=length of each loop
	#e=end, size of spiral
	#c=return to center?
	xb, yb = pyautogui.position()
	while t < e:
		x = (a + b*t) * math.cos(t)
		y = (a + b*t) * math.sin(t)
		pyautogui.dragTo(x+xb, y+yb, duration=0.1)
		t += i
	if c == True:
		pyautogui.moveTo(xb, yb)

def colorSwap(clr):
	posX, posY = pyautogui.position()
	target = pyautogui.locateOnScreen(clr+'.png')
	if target == None:
		Print('Swatch not found!')
	else:
		pyautogui.click(pyautogui.center(target))
	pyautogui.moveTo(posX, posY)

time.sleep(1)
pyautogui.click()
scale = 200
distance = 0	
shift = 10, 10

try:
	colorSwap(pyperclip.paste())
	ASpiralOut(1, 2.5, 0, 0.3, 20, True)
	pyautogui.moveRel(shift)
	# ASpiralOut(1, 2.5, 0, 0.2, 20, True)
	# colorSwap('RED')
	# pyautogui.moveRel(5, 0)
	# colorSwap('ORG')
	# ASpiralOut(1, 2.5, 0, 0.2, 20, True)
	# pyautogui.moveRel(5, 0)
	# colorSwap('YLW')
	# ASpiralOut(1, 2.5, 0, 0.2, 20, True)
except KeyboardInterrupt:
	print('\nDone.')
	
	
	
# stars = list(pyautogui.locateAllOnScreen('diamonds.png'))
# print(str(stars))
# for x in stars:
	# if x == None:
		# print('No stars found!')
	# else:
		# pyautogui.moveTo(pyautogui.center(x))
		# nspiralOut(1, 2.5, 0, 1, 50)
#nspiralOut(1, 2.5, 0, 0.1, 50)
#nspiralOut(1, 2.5, 0, 0.5, 50)
#nspiralOut(1, 2.5, 0, 1, 50)
#nspiralOut(3, 5, 0, 1, 100)
#nspiralOut(3, 7.5, 0, 1, 100)
		
#spiralOut(1, 1, 5)		
#spiralOut(1, -1, 5)
#spiralOut(-1, -1, 5)
#spiralOut(-1, 1, 5)	

# while distance > 0:
	# pyautogui.dragRel(distance, -distance, duration=0.1)   # move right
	# distance = distance - 9
	# pyautogui.dragRel(-distance, -distance, duration=0.1)   # move down
	# pyautogui.dragRel(-distance, distance, duration=0.1)  # move left
	# distance = distance - 9
	# pyautogui.dragRel(distance, distance, duration=0.1)  # move up
#pyautogui.dragRel(-distance/2, distance/2, duration=0.1)