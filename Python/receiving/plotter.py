import pyautogui, time, winsound

print('Press Ctrl-C to quit.')
try:
	while True:
		x, y = pyautogui.position()
		posStr = 'X: ' + str(x).rjust(4) +' Y: ' + str(y).rjust(4)
		pixelColor = pyautogui.screenshot().getpixel((x, y))
		posStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
		posStr += ', ' + str(pixelColor[1]).rjust(3)
		posStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
		print(posStr, end='')
		print('\b' * len(posStr), end='', flush=True)
except KeyboardInterrupt:
	winsound.Beep(500, 100)
	print('\nDone.  Last position:\n' + posStr)
	time.sleep(5)