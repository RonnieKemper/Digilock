#C:\Users\xjust\Desktop\DEV\OPS\LANG\Python\MODULES\opencv\opencvdragrect
#https://arccoder.medium.com/draggable-rectangle-in-opencv-python-dee64d8e2dc0

import numpy as np
import cv2
import os
import pyautogui
import matplotlib.pyplot as plt
import sys
from subprocess import Popen
# Set recursion limit
sys.setrecursionlimit(10 ** 9)

def addAppAccount():
	print('add app acc')
	path = input("paste the full path of the application you want to login to: ")
	#startApp = ('"' + '%s'%path + '"')
	#print(startApp)
	#os.system('start ' + startApp) #"C:\Program Files\Cakewalk\Cakewalk Core\Cakewalk.exe"
	try:
		os.startfile('%s'%path)
		#proc = Popen(['%s'%path],stdout=PIPE, stderr=PIPE)
		#lol = str("'" + '%s'%path + "'")
		#Popen(lol); Popen('%s'%path)
		image = pyautogui.screenshot() #C:\Users\xjust\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord
		plt.imshow(image)
		import selectinwindow
	except Exception as e:
		print(e)

	counter = 0
	# Initialize the  drag object
	if counter == 0:
		var = 'usrnb'
	if counter == 1:
		var = 'pwb'
	if counter == 2:
		var = 'loginbutton'
	wName = "select region"
	imageWidth = 320
	imageHeight = 240
	image = np.ones([imageHeight, imageWidth, 3], dtype=np.uint8)  # OR read an image using imread()
	image *= 255

	# Define the drag object
	rectI = selectinwindow.DragRectangle(image, wName, imageWidth, imageHeight)

	cv2.namedWindow(rectI.wname)
	cv2.setMouseCallback(rectI.wname, selectinwindow.dragrect, rectI)

	# keep looping until rectangle finalized
	while True:
	    # display the image
	    cv2.imshow(wName, rectI.image)
	    key = cv2.waitKey(1) & 0xFF

	    # if returnflag is True, break from the loop
	    if rectI.returnflag:
	        break

	print("Dragged rectangle coordinates")
	print(str(rectI.outRect.x) + ',' + str(rectI.outRect.y) + ',' + \
	      str(rectI.outRect.w) + ',' + str(rectI.outRect.h))

	# close all open windows
	#if counter == 0:
	#	usrnb = 
	cv2.destroyAllWindows()
	counter = counter + 1
addAppAccount()
'''


	usrn = input('enter username: ')
	ps = input('enter pw')

	a = usrn.encode()
	b = ps.encode()
	key = Fernet.generate_key() # Store this key or get if you already have it
	f = Fernet(key)
	password_encrypted = f.encrypt(a)
	email_encrypted = f.encrypt(b)

	cwd = os.getcwd() #cwd + '\\id\\' + 
	connection = sqlite3.connect(usrn + "keys" + ".db")
	cursor = connection.cursor()
	Store_keys = """CREATE TABLE IF NOT EXISTS
	keys(id PRIMARY KEY, key text)"""
	cursor.execute(Store_keys)
	cursor.execute("INSERT INTO keys VALUES (null, ?)", [key])
	connection.commit()
	#EncryptionDataInstance.owned_items.append(websiteName + "keys" + ".db")
	#EncryptionDataInstance.ItemsToEncrypt.append(websiteName + "keys" + ".db"); saveArray()

	params = (path, a, b)
	connection = sqlite3.connect(usrn + ".db")
	cursor = connection.cursor()
	command1 = """CREATE TABLE IF NOT EXISTS
	websiteName(id PRIMARY KEY, path text, a text, b text)"""
	cursor.execute(command1)
	cursor.execute("INSERT INTO websiteName VALUES (null, ?, ?, ?)", params)
	connection.commit()
#C:\Program Files\Cakewalk\Cakewalk Core\Cakewalk.exe
'''









#while(True):
#    image = pyautogui.screenshot()
#    #further processing
#    if finished:
#        break