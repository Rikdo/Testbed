#Auto-Receiving Encabulator 0.1
#A crudely conceived idea from Dash McLaughlin

#

import pyautogui, pyperclip, winsound, time

#INIT===============================================
PO = 4500000000
EA = 0

TEST = (360, 1065)

	#Tab coords
CHROMETAB = 0, 0
DISPLAYTAB = 0, 0
MIGOTAB = 0, 0
LABELSTAB = 0, 0
SQ01TAB = 0, 0

	#Display coords
EDITPO = 0, 0 	#Pencil/Glasses Icon
SWITCHPO = 0, 0 #orange/white icon
ENTERPO = 0, 0	#First Char of PO Entry field
STATUS = 0, 0	#Status tab
ORDERED = 0, 0
DELIVERED = 0, 0
STILLTODELIV = 0, 0

	#MIGO coords
RECEIPTDROPDOWN = 0, 0
PURCHASEORDER = 0, 0
INBOUNDDELIVERY = 0, 0
ENTERPOIB = 0, 0
DELIVERYNOTE = 0, 0
OKCHECKBOX = 0, 0
GOODSRECEIPT = 0, 0

	#Labels coords
MATDOC = (0, 0)


#Funcrtions=========================================
	#TODO: Access the log 
def display(po, ea):
	pyautogui.click(DISPLAYTAB)
	pyautogui.click(SWITCHPO)
	pyautogui.click(ENTERPO)
	pyautogui.typewriter([str(po), 'enter'])
	time.sleep(0.5)
	pyautogui.click(STATUS)
	pyautogui.moveTo(ORDERED)
	pyautogui.DragRel(-DRAG, 0)
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(0.1)
	ord = pyperclip.paste()
	pyautogui.moveTo(DELIVERED)
	pyautogui.DragRel(-DRAG, 0)
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(0.1)
	deliv = pyperclip.paste()
	pyautogui.moveTo(STILLTODELIV)
	pyautogui.DragRel(-DRAG, 0)
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(0.1)
	stilldeliv = pyperclip.paste()
	if ord == 0:
		return 'Empty/Trashed PO.'
	elif ord == deliv:
		return 'Fully received already.'
	elif stilldeliv + deliv == ord:
		if stilldeliv == ea:
			return 'Receive all'
		else:
			return 'Check for EDI'
	else:
		return 'Check for EDI'

def sq01(po, ea):
	pyautogui.click(SQ01TAB)
	
	
def migo(po, ib):
	#po = PO number or IBD number
	#ib = is this an IBD?  True/Flase
	pyautogui.click(MIGOTAB)
	pyautogui.click(RECEIPTDROPDOWN)
	if ib == True:
		pyautogui.click(INBOUNDDELIVERY)
	else:
		pyautogui.click(PURCHASEORDER)
	pyautogui.click(ENTERPOIB)
	pyautogui.typewriter([str(po), 'enter'])
	time.sleep(0.5)
	pyautogui.click(OKCHECKBOX)
	pyautogui.hotkey('ctrl', 'shift', 'f2')
	time.sleep(0.1)
	pyautogui.hotkey('ctrl', 's')
	time.sleep(1)
	pyautogui.click(GOODSRECEIPT)
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(0.1)
	gr = pyperclip.paste()
	return gr
	
def labelsGR(gr):
	pyautogui.click(LABELSTAB)
	pyautogui.click(MATDOC)
	pyautogui.typewriter([str(gr), 'enter'])
	time.sleep(0.1)
	pyautogui.hotkey('f8')
	pyautogui.hotkey('f9')
	

#Main Loop==========================================
print('Press Ctrl-C to quit.')
pyautogui.click(TEST)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.1)
print(str(pyperclip.paste()))

# try:
	# while True:
		# x, y = pyautogui.position()
		# posStr = 'X: ' + str(x).rjust(4) +' Y: ' + str(y).rjust(4)
		# pixelColor = pyautogui.screenshot().getpixel((x, y))
		# posStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
		# posStr += ', ' + str(pixelColor[1]).rjust(3)
		# posStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
		# print(posStr, end='')
		# print('\b' * len(posStr), end='', flush=True)
# except KeyboardInterrupt:
	# print('\nDone.  Last position:\n' + posStr)
	# time.sleep(5)