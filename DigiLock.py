import os, sys, stat
import json
import time
from datetime import datetime
import importlib
from importlib import reload
import getpass
import sqlite3
from sqlite3 import Error
#import operator
#import functools
import cryptography
import hashlib
from hashlib import sha256
import base64
import argon2
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC 

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView #https://stackoverflow.com/questions/56601384/kivy-unknown-class-listview-error-code/56601656#56601656 listview deprecated for recycleview
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.uix.widget import Widget
from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.uix.checkbox import CheckBox 
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelStrip
try:
    from buttondefinitions import functions
except:
    pass
from encryptiondata import EncryptionData
import six
#owned items array for use with encryption


EncryptionDataInstance = EncryptionData()
EncryptionDataInstance.dataInitialization()
#print('items')
#print(EncryptionDataInstance.ItemsToDecrypt)


if os.path.exists('buttondefinitions.py'):
	print("definitions exist")
else:
	f = open('buttondefinitions.py', 'w')
	f.write('\n' + "class functions():" + '\n')
	f.write('\t' + "def dummyfunction():" + '\n')
	f.write('\t' + '\t' + "print('forerrorhandling')" + '\n')
	f.close()
	owned_items.append('buttondefinitions.py'); saveArray()

n = datetime.now()
print("%s"%n)
f = open("mylog.txt", 'a')
if os.path.exists('MyLog.txt'):
	print("log exists")
	f.write("%s"%n + "DigiLock session started" + '\n')
	f.close()
else:
	f = open("mylog.txt", 'w')
	f.close()
	f.write("%s"%n + " NEW LOG CREATED, DID YOU DELETE THE OLD ONE?" + '\n')
	f.write("%s"%n + "  DigiLock session started" + '\n')
	f.close()
	owned_items.append('mylog.txt'); saveArray()



def SetMpw():
	if os.path.exists('User_Profile.db'):
		connection = sqlite3.connect('User_Profile.db')
		cursor = connection.cursor()
		#params = (hashed_email, hashed_MasterPassword)
		command1 = """CREATE TABLE IF NOT EXISTS
		MasterCreds(id PRIMARY KEY, hashed_email text, MasterPassword text)"""
		cursor.execute(command1)
		connection.commit()
		#loginPrompt()
	else:
		print("set your master password")
		email = getpass.getpass("Enter Email: ").encode('utf-8')
		MasterPassword = getpass.getpass("Enter MasterPassword: ").encode('utf-8')
		ConfirmMasterPassword = getpass.getpass("Confirm MasterPassword: ").encode('utf-8')
		if ConfirmMasterPassword != MasterPassword:
			print("passwords do not match")
			SetMpw()
		if ConfirmMasterPassword == MasterPassword:
			print("Passwordsmatch")
			hashed_email = hashlib.md5(email).hexdigest()
			hashed_MasterPassword = hashlib.md5(MasterPassword).hexdigest()
			connection = sqlite3.connect('User_Profile.db')
			cursor = connection.cursor()
			params = (hashed_email, hashed_MasterPassword)
			command1 = """CREATE TABLE IF NOT EXISTS
			MasterCreds(id PRIMARY KEY, hashed_email text, MasterPassword text)"""
			cursor.execute(command1)
			cursor.execute("INSERT INTO MasterCreds VALUES (null, ?, ?)", params)
			connection.commit()
			#logf.write("%s"%n + " NEW MASTERPASSWORD CREATED" + '\n'); logf.close()
			owned_items = EncryptionData.getOwnedObjects()
			owned_items.append('User_Profile.db'); EncryptionDataInstance.saveArray()
		#print(hashed_MasterPassword)
		#database #connection.SetPassword("password")
		#print(hashed_email)

SetMpw()
#def loginPrompt():
#	global failcounter
#loginPrompt()
class mykdf():
	def __init__(self, **kwargs): #
		# super function can be used to gain access  
		# to inherited methods from a parent or sibling class  
		# that has been overwritten in a class object.  
		super(mykdf, self).__init__(**kwargs)
		mykdf.failcounter = 0
	def generate_key_derivation(instance): #put function into gui class in backbone
		#global masterkey

		def loginPrompt():
			if os.path.exists("salt.py"):	
				with open("salt.py", "rb") as f:
					salt = f.read() #.encode(); #salt = str(salt)
					f.close(); print(salt)
					owned_items = EncryptionData.getOwnedObjects()
					owned_items.append("salt.py"); EncryptionDataInstance.saveArray()
			else:
				owned_items = EncryptionData.getOwnedObjects()
				salt = os.urandom(16); #.decode()
				with open("salt.py", "wb") as f:
					f.write(salt)
					f.close()
				salt = open("salt.py").read().encode()
				#type(salt)
				owned_items.append("salt.py"); EncryptionDataInstance.saveArray()
			print("Enter your credentials, the screen will not show them.")
			#email = getpass.getpass("Enter Email: ").encode('utf-8')
			#makesalt()
			MasterPassword = getpass.getpass("Enter MasterPassword: ").encode() #'utf-8'
			#hashed_email = hashlib.md5(email).hexdigest()
			hashed_MasterPassword = hashlib.md5(MasterPassword).hexdigest()
			connection = sqlite3.connect('User_Profile.db')
			cursor = connection.cursor()
			cursor.execute("SELECT MasterPassword FROM MasterCreds")
			results = cursor.fetchone()
			print(results)
			tup = results
			print(tup)
			final = ''.join(tup)
			print(salt)
			if final == hashed_MasterPassword: 
				kdf = PBKDF2HMAC( #key derivation function
					algorithm=hashes.SHA256(), #parameter inheritance/definitions, keyword args
					length=32,
					salt=salt,
					iterations=100000,
					backend=default_backend()
				)
				masterkey = base64.urlsafe_b64encode(kdf.derive(final.encode())); print(masterkey) #final.encode()
				mykdf.masterkey = masterkey
				#verify key
				hashed_key = hashlib.md5(masterkey).hexdigest()
				conn = sqlite3.connect('User_Profile.db')
				cursor = connection.cursor()
				command1 = """CREATE TABLE IF NOT EXISTS
				VerifyKey(id PRIMARY KEY, hashed_key text)"""
				cursor.execute(command1)
				params = json.dumps(hashed_key); # print(params); print(type(params))
				try:
					cursor.execute("SELECT hashed_key FROM VerifyKey")
					results = cursor.fetchone()
					results = json.dumps(results); print(results)
					#results = results; #print(tup)
					results = str(results); print(results)
					hashed_keydb = results[4:-4]; print(results)
					#results = str(results)
					#hashed_keydb = json.loads(results)
					#hashed_keydb = results[2:-3]; #https://stackoverflow.com/questions/21058935/python-json-loads-shows-valueerror-extra-data/51830719
					#hashed_key = '"' + hashed_key + '"'
					print('hashed_keydb'); print(hashed_keydb); print('hashed_key'); print(hashed_key) #''.join(results)
					connection.commit();
				except:
					#params = json.dumps(hashed_key); print(params)
					print('error')
				if hashed_keydb == hashed_key:
					print("ACCESS GRANTED")
				else:
					cursor.execute("INSERT INTO VerifyKey VALUES (null, ?)", (params,)) #https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
					cursor.execute("SELECT hashed_key FROM VerifyKey")
					results = cursor.fetchone()
					tup = results
					hashed_keydb = ''.join(tup)
					#hashed_key = str(hashed_key)
					connection.commit(); print(hashed_keydb); print(hashed_key)
					if hashed_keydb == hashed_key:
						print("ACCESS GRANTED")
					else:
						print('possible key corruption, try again')
						loginPrompt()
				#return masterkey
				#logf.write("%s"%n + " LOGGED IN WITH " + failcounter + " FAILED LOGIN ATTEMPTS" + '\n')
				#logf.close()
			elif hashed_MasterPassword != final: 
				print("hacker!!")
				n = datetime.now()
				mykdf.failcounter = mykdf.failcounter + 1
				print(mykdf.failcounter)
				#del email
				del hashed_MasterPassword
				loginPrompt()
				#generate_key_derivation()
				#exit()
			if mykdf.failcounter > 50: 
				print("you are being brute forced")
				time.sleep(5)
				exit()
		loginPrompt()
		#print(hashed_MasterPassword)
		#print(hashed_email) 
		#plaintext_password = getpass.getpass("Enter MasterPassword: ") #MasterPassword #.encode('utf-8')
		#print(plaintext_password)
		#masterkey = base64.urlsafe_b64encode(kdf.derive(plaintext_password.encode()))
		#loginPrompt()
		#masterkey = base64.urlsafe_b64encode(kdf.derive(plaintext_password.encode()))
		#kdf.verify(plaintext_password, masterkey)
		#del plaintext_password
		#print(MasterPassword)
		#print(masterkey)
		#mykdf.masterkey = masterkey
			#return masterkey
instance = mykdf()
instance.generate_key_derivation()
#mykdf.loginPrompt()
#print(instance)
#type(instance)

class encryptobj(mykdf):
	def __init__(self, **kwargs):
		super(encryptobj, self).__init__(**kwargs)
	#@classmethod
	def encryptor(instance): #, value_to_encrypt #doi = f.decrypt(owned_items) #array first
		#print("masterkey")
		f = Fernet(instance.masterkey)
		print(f)
		EncryptionDataInstance.dataInitialization()
		owned_items = EncryptionData.getOwnedObjects()
		ItemsToEncrypt = EncryptionData.getItemsToEncrypt()
		ItemsToDecrypt = EncryptionData.getItemsToDecrypt()
		print("owned_items = ..."); print(owned_items); print("ItemsToEncrypt = ..."); print(ItemsToEncrypt); print(type(ItemsToEncrypt))
		for i in ItemsToEncrypt: #verify file is owned by digilock
			print(i)
			try:
				if ItemsToDecrypt.index(i) == True:
					continue
			except:
				print('...skipping')
			#token = base64.urlsafe_b64decode(i)
			#if os.path.exists(i): #os.path.exists(owned_items.index(i)): # == True: # & i.encrypted == False: #if ItemsToEncrypt[i] does exist in Owned_items: proceed with cryptography
			try: 
				with open(i, "rb") as g: #create cipher
					fd = g.read() #fd
					#print(type(fd))
					c = f.encrypt(fd) #base64.decode(f.encrypt(fd))
					#print(c)
					#c = f.encrypt(fd)
					g.close()
				with open(i, "wb") as h: #write cipher
					h.write(c)
					h.close()
					#print(c)
					EncryptionDataInstance.ItemsToEncrypt.remove(i); #EncryptionDataInstance.saveArray()
					#print("ItemsToEncrypt" + ItemsToEncrypt)
					#print("ItemsToDecrypt" + ItemsToDecrypt)
			except InvalidToken:
				print("InvalidToken")
				
				EncryptionDataInstance.ItemsToDecrypt.append(i)
				EncryptionDataInstance.ItemsToEncrypt.remove(i); #EncryptionDataInstance.saveArray()
				#return b'' 
				continue
			#else: #elif: os.path.exists(owned_items.index(i)) == False:  #if ItemsToEncrypt[i] not exist in Owned_items: pass
			#	continue
		print('ENCRYPTION FINISHED')
		EncryptionDataInstance.saveArray()
		print(ItemsToEncrypt)
#EncryptionInstance = encryptobj() #moving this line to reinit on each action

class decryptobj(mykdf): #changed from encrypted_key to value_to_encrypt to var #mykdf
	def __init__(self, **kwargs):
		super(decryptobj, self).__init__(**kwargs)
	#@classmethod	
	def decryptor(instance): #https://github.com/ansible/awx/issues/4406
		#print(instance)
		#print(instance.masterkey)
		#print(mykdf.masterkey)
		#global instance.masterkey
		#print(instance.masterkey)
		f = Fernet(instance.masterkey); print(f)
		EncryptionDataInstance.dataInitialization()
		owned_items = EncryptionDataInstance.getOwnedObjects()
		ItemsToEncrypt = EncryptionDataInstance.getItemsToEncrypt(); print(ItemsToEncrypt)
		ItemsToDecrypt = EncryptionDataInstance.getItemsToDecrypt()
		#EncryptionData.ItemsToEncrypt = []
		print("owned_items = ..."); print(owned_items); print("ItemsToDecrypt = ..."); print(type(ItemsToDecrypt)); print(ItemsToDecrypt)
		for i in ItemsToDecrypt:
			print(i)
			#token = base64.urlsafe_b64decode(i)
			#if os.path.exists(i):
			try:
				with open(i, "rb") as g: # read the encrypted data
					fd = g.read(); #print(fd) #.read()
					#print(fd)
					#try:
					c = base64.urlsafe_b64decode(fd); #print(c); 
					print(type(c))
					#except:
					#	pass
					dd = f.decrypt(c) #decrypt data #fd f.decrypt(bytes(fd,'utf-8')) #str(six.indexbytes(fd, 0)).encode()
					g.close()
				with open(i, "wb") as h:  # write the original file
					h.write(dd)
					h.close()
					ItemsToEncrypt.append(i); 
					ItemsToDecrypt.remove(i); 
				#print("ItemsToEncrypt: " ItemsToEncrypt)
				#print("ItemsToDecrypt" + ItemsToDecrypt)
			except:
				print('InvalidToken')
				#return b''
				#ItemsToEncrypt.append(i); 
				#ItemsToDecrypt.remove(i); #EncryptionDataInstance.saveArray()
				continue
			#else:
				#print('not exist') 
				#print(i + " does not exist, would you like to recover it? y/n: ")
				#option = input(); #if option == 'y':;'\n' + '\t' addWebAccount()
				#continue
			#if ItemsToDecrypt != '[]':
			#	continue
		EncryptionData.ItemsToEncrypt = ItemsToEncrypt
		EncryptionData.ItemsToDecrypt = ItemsToDecrypt
		EncryptionDataInstance.saveArray()
		print('DECRYPTION FINISHED')
		print('ItemsToDecrypt = '); print(ItemsToDecrypt); print('EncryptionData.ItemsToEncrypt = '); print(EncryptionData.ItemsToEncrypt)



#instantiating instance of class to call method as attribute
#DecryptionInstance = decryptobj()
#myinstance.decryptor()
#print(EncryptionDataInstance.ItemsToEncrypt)
#print(EncryptionDataInstance.ItemsToDecrypt)
#print(EncryptionDataInstance.owned_items)
#attrib(instance)
#GUI SHOULD BOOT HERE
# Loading Multiple .kv files  
Builder.load_file('Emails.kv') 
#Builder.load_file('Business.kv')
Builder.load_file('Financial.kv') 
Builder.load_file('Legal.kv')
Builder.load_file('Socialmedia.kv')
Builder.load_file('Games.kv')
Builder.load_file('Blogs.kv')
Builder.load_file('All.kv') 
  
class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        def switchtoaccountscreen(self, *args):
            if self.manager.current != 'Accounts':
                self.manager.current = 'Accounts'
        def switchtosettingsscreen(self, *args):
            if self.manager.current != 'settings':
                self.manager.current = 'settings'
        def switchtoactionssscreen(self, *args):
            if self.manager.current != 'actions':
                self.manager.current = 'actions' 
        def switchtoBrowserSelectionScreen(self, *args): 
        	self.manager.current = 'BrowserSelectionScreen' 
# Creating main kv file class 
#class main_kv(TabbedPanel, GridLayout, Screen, App): 
#    pass
#class MyLayout(FloatLayout):
#    pass
#class Box3(TabbedPanel, GridLayout, Screen, App):
#	pass
class BrowserSelectionScreen(GridLayout, Screen):
    #container = ObjectProperty(None)
    def __init__(self, **kwargs): #
        # super function can be used to gain access  
        # to inherited methods from a parent or sibling class  
        # that has been overwritten in a class object.  
        super(BrowserSelectionScreen, self).__init__(**kwargs)
        BrowserSelectionScreen.browser = 'Chrome' #default
        self.cols = 1 
        self.settingsb = Button(text="Back", font_size=20, size_hint_y=None, height=40)
        self.settingsb.bind(on_press=self.switchtosettingsscreen)
        self.add_widget(self.settingsb)

        self.Chromeb = Button(text="Chrome", font_size=20, size_hint_y=None, height=40)
        #AccountButton = Button(text="Accounts", font_size=20, size_hint_y=None, height=40)
        self.Chromeb.bind(on_press=self.SelectChromeBrowser)
        self.add_widget(self.Chromeb)
        #layout.add_widget(self.AccountButton)
        #layout.add_widget(AccountButton)

        self.FireFoxb = Button(text="Firefox", font_size=20, size_hint_y=None, height=40)
        #addaccb = Button(text="add web account", font_size=20, size_hint_y=None, height=40)
        self.FireFoxb.bind(on_press=self.SelectFirefoxBrowser)
        self.add_widget(self.FireFoxb)
    def SelectChromeBrowser(self, *args):	
    	BrowserSelectionScreen.browser = 'Chrome'
    	print(self.browser)
    def SelectFirefoxBrowser(self, *args):
    	BrowserSelectionScreen.browser = 'firefox'
    	print(self.browser)
    def switchtosettingsscreen(self, *args):
        if self.manager.current != 'settings':
            self.manager.current = 'settings'

    '''
    if BrowserSelectionScreen.Browser = 'Chrome':
    	import ChromeHeader
    if BrowserSelectionScreen.Browser = 'Firefox':
		import MozillaHeader
	'''
class SettingsScreen(GridLayout, Screen, mykdf):
    #container = ObjectProperty(None)
    def __init__(self, **kwargs): #
        # super function can be used to gain access  
        # to inherited methods from a parent or sibling class  
        # that has been overwritten in a class object.  
        super(SettingsScreen, self).__init__(**kwargs)
        #layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        #Clock.schedule_once(self.setup_scrollview, 1)

        self.cols = 2
        #self.bind(minimum_height=self.height)
        #GridLayout(cols=1, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        #GridLayout.bind(minimum_height=layout.setter('height'))

        self.addaccb = Button(text="add web account", font_size=20, size_hint_y=None, height=40)
        #addaccb = Button(text="add web account", font_size=20, size_hint_y=None, height=40)
        self.addaccb.bind(on_press=self.webaccPressed)
        self.add_widget(self.addaccb)
        #layout.add_widget(self.addaccb)
        #layout.add_widget(addaccb)

        self.AccountButton = Button(text="Web Accounts", font_size=20, size_hint_y=None, height=40)
        #AccountButton = Button(text="Accounts", font_size=20, size_hint_y=None, height=40)
        self.AccountButton.bind(on_press=self.switchtoaccountscreen)
        self.add_widget(self.AccountButton)
        #layout.add_widget(self.AccountButton)
        #layout.add_widget(AccountButton)

        self.addAppAccountb = Button(text="add app account", font_size=20, size_hint_y=None, height=40)
        addaccb = Button(text="add app account", font_size=20, size_hint_y=None, height=40)
        self.addAppAccountb.bind(on_press=self.addAppAccount)
        self.add_widget(self.addAppAccountb)

        self.appaccb = Button(text="App Accounts", font_size=20, size_hint_y=None, height=40)
        #addaccb = Button(text="add web account", font_size=20, size_hint_y=None, height=40)
        self.appaccb.bind(on_press=self.switchtoAppaccountscreen)
        self.add_widget(self.appaccb)
        #layout.add_widget(self.addaccb)
        #layout.add_widget(addaccb)

        self.setBrowserb = Button(text="choose browser", font_size=20, size_hint_y=None, height=40)
        #addaccb = Button(text="add web account", font_size=20, size_hint_y=None, height=40)
        self.setBrowserb.bind(on_press=self.switchtoBrowserSelectionScreen)
        self.add_widget(self.setBrowserb)

        self.mfab = Button(text="Multi-Factor authentication", font_size=20, size_hint_y=None, height=40)
        #mfab = Button(text="Multi-Factor authentication", font_size=20, size_hint_y=None, height=40)
        #self.mfab.bind(on_press=self.mfa) #phoneNumber
        self.add_widget(self.mfab)
        #layout.add_widget(self.mfab)
        #layout.add_widget(mfab)

        #add identity

        self.updateb = Button(text="update", font_size=20, size_hint_y=None, height=40)
        #donateb = Button(text="donate", font_size=20, size_hint_y=None, height=40)
        self.updateb.bind(on_press=self.checkforupdates)
        self.add_widget(self.updateb)
        #layout.add_widget(self.donateb)
        #layout.add_widget(donateb)

        self.ResetPasswordb = Button(text="reset MasterPassword", font_size=20, size_hint_y=None, height=40)
        #donateb = Button(text="donate", font_size=20, size_hint_y=None, height=40)
        self.ResetPasswordb.bind(on_press=self.ResetPassword)
        self.add_widget(self.ResetPasswordb)
        #layout.add_widget(self.donateb)
        #layout.add_widget(donateb)

        self.quitb = Button(text="Quit", font_size=20, size_hint_y=None, height=40)
        #quitb = Button(text="Quit", font_size=20, size_hint_y=None, height=40)
        self.quitb.bind(on_press=self.closeapp)
        self.add_widget(self.quitb)
        #self.add_widget(ScrollView(size_hint=(1, None), size=(Window.width, Window.height)))
        #layout.add_widget(self.quitb)
        #root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        #root.add_widget(layout)
        #sv = ScrollView(size_hint=(self.height, self.width), height=self.height)
        #self.add_widget(sv)

        #root.add_widget(layout)
        #runTouchApp(root)

        # These value are needed to set the width of self.movable_tab_strip, but
        # they aren't always available when self.first is called below
        #self._tab_strip.bind(width=self.tab_strip_width_changed)
        #self.bind(width=self.panel_width_changed)

        #Clock.schedule_once(self.first)
    #def setup_scrollview(self, dt):
    #    self.container.bind(minimum_height=self.container.setter('height'))
    #    self.add_text_inputs()
    def ResetPassword(self, *args):
        print('password reset')
        DecryptionInstance = decryptobj()
        DecryptionInstance.decryptor()
        print('enter your current MasterPassword')
        oldMPW = getpass.getpass("Enter MasterPassword: ").encode() #'utf-8'
        #hashed_email = hashlib.md5(email).hexdigest()
        hashed_MasterPassword = hashlib.md5(oldMPW).hexdigest()
        connection = sqlite3.connect('User_Profile.db')
        cursor = connection.cursor()
        cursor.execute("SELECT MasterPassword FROM MasterCreds")
        results = cursor.fetchone()
        print(results)
        tup = results
        print(tup)
        final = ''.join(tup)
        if hashed_MasterPassword == final:
            print('authenticated, enter your new password')
            newMPW = getpass.getpass("enter new MasterPassword: ").encode()
            confirmnewMPW = getpass.getpass("enter new MasterPassword: ").encode()
            if newMPW == confirmnewMPW:
                hashed_MasterPassword = hashlib.md5(newMPW).hexdigest()
                cursor.execute("SELECT hashed_email FROM MasterCreds")
                results = cursor.fetchone()
                print(results)
                tup = results
                print(tup)
                email = ''.join(tup)
                connection.commit()
                connection.close()
                os.remove('User_Profile.db')
                connection = sqlite3.connect('User_Profile.db')
                cursor = connection.cursor()
                params = (email, hashed_MasterPassword)
                command1 = """CREATE TABLE IF NOT EXISTS
                MasterCreds(id PRIMARY KEY, hashed_email text, MasterPassword text)"""
                cursor.execute(command1)
                cursor.execute("INSERT INTO MasterCreds VALUES (null, ?, ?)", params)
                connection.commit()

                instance = mykdf()
                instance.generate_key_derivation()

    def checkforupdates(self, instance): #, value
        exec(open("checkDriver.py").read())
    
    def switchtoAppaccountscreen(self, *args):
    	if self.manager.current != 'AppAccounts':
            self.manager.current = 'AppAccounts'
    def switchtoaccountscreen(self, *args):
        if self.manager.current != 'Accounts':
            self.manager.current = 'Accounts'
    def switchtosettingsscreen(self, *args):
        if self.manager.current != 'settings':
            self.manager.current = 'settings'
    def switchtoBrowserSelectionScreen(self, *args): 
        self.manager.current = 'BrowserSelectionScreen'
    def webaccPressed(self, instance): #addWebAccount
        print("loading account")
        addWebAccount()
    def mfa(self, instance):
        print('future update')
    def addAppAccount(self, instance):
        print("paste the full path of the application you want to login to: ")
        path = input()
    def setBrowser(self, instance):
        print('future update')
    def moveto(self, *args):
        print("future update")
    def deleteWebAccounts(self, *args):
        print('future update')
        #def changeScreen(self):
        #    if self.manager.current == 'SettingsScreen':
        #        self.manager.current = 'AccountsScreen'
        #    if self.manager.current == 'AccountsScreen':
        #        self.manager.current = 'SettingsScreen'
    def closeapp(self, *args):
        EncryptionInstance = encryptobj()
        EncryptionInstance.encryptor()
        #DecryptionInstance = decryptobj()
        #DecryptionInstance.decryptor()
        exit()
#class DATA():
class AppAccountsScreenApp(TabbedPanel, GridLayout, Screen, App, functions, mykdf): #functions
	#accounts = ObjectProperty(None)
	def __init__(self, **kwargs):
		# super function can be used to gain access  
		# to inherited methods from a parent or sibling class  
		# that has been overwritten in a class object.
		self.cols = 3 
		super(AccountsScreenApp, self).__init__(**kwargs)
		#print(functions)
		#FreshHeader()
		self.settingsb = Button(text="Settings", font_size=20, size_hint_y=None, height=40)
		self.settingsb.bind(on_press=self.switchtosettingsscreen)
		self.add_widget(self.settingsb)

		self.initialTabHeight = None
		self.myTabsList = None
		self.start_top = None
		self.tabs_showing = True

		# this TabbedPanelStrip will be a copy of the real one (self._tab_strip)
		self.tmp_tab_strip = TabbedPanelStrip(
			tabbed_panel=self,
			rows=1, size_hint=(None, None),
			height=self.tab_height, width=self.tab_width)

		# this is the movable Widget that contains the tabs
		self.movable_tab_strip = ScrollView(size_hint=(None, None), height=self.tab_height)

		# These value are needed to set the width of self.movable_tab_strip, but
		# they aren't always available when self.first is called below
		self._tab_strip.bind(width=self.tab_strip_width_changed)
		self.bind(width=self.panel_width_changed)

		Clock.schedule_once(self.first)

	def tab_strip_width_changed(self, instance, new_width):
		self.movable_tab_strip.width = min(self.tmp_tab_strip.width, self.width)

	def panel_width_changed(self, instance, new_width):
		self.movable_tab_strip.width = min(self.tmp_tab_strip.width, self.width)

	def first(self, *args):
		# show tab2, so that the Button will be available
		#self.switch_to(self.parent.ids.tab2)

		# save some info
		self.initialTabHeight = self.tab_height
		self.myTabsList = self.tab_list.copy()

		tsw = 99
		for tab in self.myTabsList:
			if tab.size_hint_x:
				tsw += 100
			else:
				tsw += tab.width
		self.tmp_tab_strip.width = tsw
		self.movable_tab_strip.add_widget(self.tmp_tab_strip)

	def do_clear_widgets(self, *args):
		# eliminate the tabs and populate the moveable_tab_strip
		self.movable_tab_strip.width = min(self.tmp_tab_strip.width, self.width)
		self.tab_height = 0
		self.clear_tabs()
		for tab in reversed(self.myTabsList):
			self.tmp_tab_strip.add_widget(tab)
		self.tabs_showing = False

	def do_progress(self, animation, widget, progression):
		# grow the tab height when the moveable_tab_strip impinges on the TabbedPanel
		# this has the effect of appearing to shrink the TappedPanel to the size it will have when the tabs are replaced
		if self.start_top > self.movable_tab_strip.y:
			self.tab_height = self.start_top - self.movable_tab_strip.y

	#def do_replace_tabs(self, *args):
		# replace the moveable_tab_trip with the actual tabs
		#self.tmp_tab_strip.clear_widgets()
		#for tab in reversed(self.myTabsList):
		#    self.add_widget(tab)
		#self.tab_height = self.initialTabHeight
		#self.parent.remove_widget(self.movable_tab_strip, App.get_running_app().root_window.height) #, App.get_running_app().root_window.height

	def do_tab_toggle(self, *args):
		if self.tabs_showing:
			pass
			#self.do_clear_widgets()
		else:
			self.anim = Animation(pos=(self.x+2, self.y + self.height - self.movable_tab_strip.height))
			#self.movable_tab_strip.pos = (self.x + 2)
			self.start_top = self.top
			#self.parent.add_widget(self.movable_tab_strip)
			self.anim.bind(on_progress=self.do_progress)
			self.anim.bind(on_complete=self.do_replace_tabs)
			self.anim.start(self.movable_tab_strip)
			self.tabs_showing = True
		#do_tab_toggle(self)
	#thePanel.do_tab_toggle()
	# Callback for the checkbox 
	def switchtoaccountscreen(self, *args):
		if self.manager.current != 'Accounts':
			self.manager.current = 'Accounts'
	def switchtosettingsscreen(self, *args):
		if self.manager.current != 'settings':
			self.manager.current = 'settings'
	def ResetWebAccountPasswords(self):
		print("future update")
		#
		#SampBoxLayout.append(buttondefinitions)
	#def webaccPressed(self, instance): #addWebAccount
	#	print("loading account")
	#	addWebAccount()

class AccountsScreenApp(TabbedPanel, GridLayout, Screen, App, functions, mykdf): #functions
	#accounts = ObjectProperty(None)
	def __init__(self, **kwargs):
		# super function can be used to gain access  
		# to inherited methods from a parent or sibling class  
		# that has been overwritten in a class object.
		self.cols = 3 
		super(AccountsScreenApp, self).__init__(**kwargs)
		#print(functions)
		#FreshHeader()
		self.settingsb = Button(text="Settings", font_size=20, size_hint_y=None, height=40)
		self.settingsb.bind(on_press=self.switchtosettingsscreen)
		self.add_widget(self.settingsb)

		self.initialTabHeight = None
		self.myTabsList = None
		self.start_top = None
		self.tabs_showing = True

		# this TabbedPanelStrip will be a copy of the real one (self._tab_strip)
		self.tmp_tab_strip = TabbedPanelStrip(
			tabbed_panel=self,
			rows=1, size_hint=(None, None),
			height=self.tab_height, width=self.tab_width)

		# this is the movable Widget that contains the tabs
		self.movable_tab_strip = ScrollView(size_hint=(None, None), height=self.tab_height)

		# These value are needed to set the width of self.movable_tab_strip, but
		# they aren't always available when self.first is called below
		self._tab_strip.bind(width=self.tab_strip_width_changed)
		self.bind(width=self.panel_width_changed)

		Clock.schedule_once(self.first)

	def tab_strip_width_changed(self, instance, new_width):
		self.movable_tab_strip.width = min(self.tmp_tab_strip.width, self.width)

	def panel_width_changed(self, instance, new_width):
		self.movable_tab_strip.width = min(self.tmp_tab_strip.width, self.width)

	def first(self, *args):
		# show tab2, so that the Button will be available
		#self.switch_to(self.parent.ids.tab2)

		# save some info
		self.initialTabHeight = self.tab_height
		self.myTabsList = self.tab_list.copy()

		tsw = 99
		for tab in self.myTabsList:
			if tab.size_hint_x:
				tsw += 100
			else:
				tsw += tab.width
		self.tmp_tab_strip.width = tsw
		self.movable_tab_strip.add_widget(self.tmp_tab_strip)

	def do_clear_widgets(self, *args):
		# eliminate the tabs and populate the moveable_tab_strip
		self.movable_tab_strip.width = min(self.tmp_tab_strip.width, self.width)
		self.tab_height = 0
		self.clear_tabs()
		for tab in reversed(self.myTabsList):
			self.tmp_tab_strip.add_widget(tab)
		self.tabs_showing = False

	def do_progress(self, animation, widget, progression):
		# grow the tab height when the moveable_tab_strip impinges on the TabbedPanel
		# this has the effect of appearing to shrink the TappedPanel to the size it will have when the tabs are replaced
		if self.start_top > self.movable_tab_strip.y:
			self.tab_height = self.start_top - self.movable_tab_strip.y

	#def do_replace_tabs(self, *args):
		# replace the moveable_tab_trip with the actual tabs
		#self.tmp_tab_strip.clear_widgets()
		#for tab in reversed(self.myTabsList):
		#    self.add_widget(tab)
		#self.tab_height = self.initialTabHeight
		#self.parent.remove_widget(self.movable_tab_strip, App.get_running_app().root_window.height) #, App.get_running_app().root_window.height

	def do_tab_toggle(self, *args):
		if self.tabs_showing:
			pass
			#self.do_clear_widgets()
		else:
			self.anim = Animation(pos=(self.x+2, self.y + self.height - self.movable_tab_strip.height))
			#self.movable_tab_strip.pos = (self.x + 2)
			self.start_top = self.top
			#self.parent.add_widget(self.movable_tab_strip)
			self.anim.bind(on_progress=self.do_progress)
			self.anim.bind(on_complete=self.do_replace_tabs)
			self.anim.start(self.movable_tab_strip)
			self.tabs_showing = True
		#do_tab_toggle(self)
	#thePanel.do_tab_toggle()
	# Callback for the checkbox 
	def switchtoaccountscreen(self, *args):
		if self.manager.current != 'Accounts':
			self.manager.current = 'Accounts'
	def switchtosettingsscreen(self, *args):
		if self.manager.current != 'settings':
			self.manager.current = 'settings'
	def ResetWebAccountPasswords(self):
		print("future update")
		#
		#SampBoxLayout.append(buttondefinitions)
	#def webaccPressed(self, instance): #addWebAccount
	#	print("loading account")
	#	addWebAccount()

	#print(instance.encryptor)
	#owned_items.append("GithubMain.py")
	def Loginpressed(self): #, masterkey #, instance, masterkey #, decryptor, encryptor
		#self.lbl_active.text ="Logging in"
		#print(decryptor())
		#print(decryptor)
		#decryptor()
		DecryptionInstance = decryptobj()
		DecryptionInstance.decryptor()
		#f = open("chromeHeader.py", "a"); f.write('\n' + "FreshHeader()"); f.close()
		#exec(open("chromeHeader.py").read())

		
		if BrowserSelectionScreen.browser == 'Chrome':
			import chromeHeader
		if BrowserSelectionScreen.browser == 'Firefox':
			import MozillaHeader
		
		#import chromeHeader
		#from chromeHeader import ChromeHeader
		#from chromeHeader import Xpath_Util
		#serialize()
		'''
		def serialize():
			EncryptionDataInstance = EncryptionData()
			EncryptionDataInstance.getactiveAccounts(); print('chromeheader active accounts:'); print(EncryptionData.activeAccounts)
			gbl = globals()
			for i in EncryptionData.activeAccounts: #EncryptionData.
				#moduleToImport = 'parentDirectory.'+toImport
				print(i)
				gbl[i] = importlib.import_module(i) #https://stackoverflow.com/questions/31661188/import-files-in-python-with-a-for-loop-and-a-list-of-names
				#from {}.format(i) import login # from i import login
				account = login() #each account has the same class name...lambda?
				xpath_obj = Xpath_Util()
				driver = ChromeHeader.MyBrowserInstance
				url = login.url
				driver.execute_script("window.open('','_blank');")
				driver.get(url)
				page = driver.execute_script("return document.body.innerHTML").\
				encode('utf-8').decode('latin-1')#returns the inner HTML as a string
				soup = BeautifulSoup(page, 'html.parser')
				if xpath_obj.generate_xpath(soup) is False:
					print ("No XPaths generated for the URL:%s"%url)
		serialize()
		'''
		#import chromeHeader; serialize()
		#EncryptionInstance = encryptobj()
		#EncryptionInstance.encryptor()

		#connection = sqlite3.connect("OwnedObjects.db")
		#cursor = connection.cursor()
		#comm = """DELETE FROM CRICKETERS WHERE LAST_NAME = 'githubmain'"""
		#cursor.execute(comm)
		#connection.commit()
		#FreshHeader()
		exit()
		#Array__init__.py code removed from here, added to buttondefinitions 
#//*[@id="login"]/form/div[4]/input[12]
#/html/body/div[3]/main/div/form/div[4]/input[12]
	# Callback for the checkbox 
	def checkbox_click(self, instance): 
		if value is True: 
			print("Checkbox Checked") 
		else: 
			print("Checkbox Unchecked") 
#SampBoxLayout.append(buttondefinitions)
#creates a fresh chromeHeader which has selenium driver config
#def FreshHeader():
	#f = open('chromeHeader.py', "w+")#create if not exist
	#f = open('chromeHeader.py', "a+")
	#f.write("import selenium" + '\n')
	#f.write("from selenium import webdriver" + '\n')
	#f.write("from selenium.webdriver.common.keys import Keys" + '\n')
	#f.write("import sqlite3" + '\n')
	#f.write('from bs4 import BeautifulSoup' + '\n')
	#f.write('import re' + '\n')
	#f.write('import os' + '\n')
	#f.write("from locate_xpath import Xpath_Util" + '\n')
	#f.write("class ChromeHeader(selenium, webdriver):" + '\n')
	#f.write('\t' + 'def __init__(self, **kwargs):'+ '\n')
	#f.write('\t' + '\t' + 'super(ChromeHeader, self).__init__(**kwargs)' +'\n')
	#f.write('\t' + 'webdriver = WebDriver()' + '\n')
	#f.write('\t' + 'driver = webdriver.Chrome()' + '\n') #
	#cwd = os.getcwd()
	#f.write('\t' + 'driver = webdriver.Chrome(executable_path=r' + "'" + cwd + '\chromedriver.exe' + "')" '\n')
	#f.write('\t' + "def get_browser():" + '\n')
	#f.write('\t' + '\t' + "if " + '"' + "browser" + '"' + " not in g:" + '\n')
	#f.write('\t' + '\t' + '\t' + "options = webdriver.ChromeOptions()" + '\n')
	#f.write('\t' + '\t' + '\t' + "options.add_argument(" + '"' + "no-sandbox" + '"' + ")" + '\n')
	#f.write('\t' + '\t' + '\t' + "options.add_argument(" + '"' + "--disable-dev-shm-usage" + '"' + ")" + '\n')
	#f.write('\t' + '\t' + '\t' + "options.add_argument(" + '"' + "--aggressive-cache-discard" + '"' + ")" + '\n')
	#f.write('\t' + '\t' + '\t' + "options.add_argument(" + '"' + "--no-displaying-insecure-content" + '"' + ")" + '\n')
	#f.write('\t' + '\t' + '\t' + "options.add_argument(" + '"' + "--incognito" + '"' + ")" + '\n')
	#f.write('\t' + '\t' + '\n' + '\n')
	#f.write('\t' + '\t' + '\t' + "host = " + "'" + "chrome" + "'" + " if current_app.config["+ '"DEBUG"' + "] else " + "'" + "127.0.0.1" + "'" + '\n')
	#f.write('\t' + '\t' + '\t' + "g.browser = webdriver.Remote(" + '\n')
	#f.write('\t' + '\t' + '\t' + '\t' +"command_executor=f" + '"' + "https://" + "{" + "host}" + ":4444/wd/hub" + '",' + '\n')
	#f.write('\t' + '\t' + '\t' + '\t' + "desired_capabilities=DesiredCapabilities.CHROME," + '\n')
	#f.write('\t' + '\t' + '\t' + '\t' + "options=options," + '\n')
	#f.write('\t' + '\t' + '\t' + ")" + '\n')
	#f.write('\t' + '\t' + "return g.browser" + '\n')
	#f.write('\t' + 'get_browser()' + '\n')
	#f.write('\t' + 'driver = webdriver.Chrome()' + '\n')
	#f.write('ChromeHeader()' + '\n')
	#f.write('driver = webdriver.Chrome()' + '\n')
	#f.close()
#the functions below write the dynamic programs needed to operate this app


def addWebAccount():
	print("the screen will not show what you type")
	websiteName = input("Enter a title for the account log in button: ")
	#print("https means the connection is encrypted, http is not. make sure your link is HTTPS")
	LoginUrl = getpass.getpass("enter url, it will not show: ")
	email = getpass.getpass("Enter username: ")
	password = getpass.getpass("Enter Password: ")
	#loginboxxpath = getpass.getpass("paste loginbox XPATH: ")
	#passwordboxxpath = getpass.getpass("Paste passwordbox XPATH: ")
	#Loginbuttonxpath = getpass.getpass("Paste login button XPATH: ")

	a = password.encode()
	b = email.encode()
	c = LoginUrl.encode()
	key = Fernet.generate_key() # Store this key or get if you already have it
	f = Fernet(key)
	password_encrypted = f.encrypt(a)
	email_encrypted = f.encrypt(b)
	LoginUrl_encrypted = f.encrypt(c)
	#decrypted = f.decrypt(password_encrypted)
	#decrypted = f.decrypt(encode)
	#password == encrypted

	#store and retrieve keys
	EncryptionDataInstance = EncryptionData()
	EncryptionDataInstance.dataInitialization()
	#owned_accounts = EncryptionDataInstance.getowned_accounts()
	print(EncryptionData.owned_accounts)
	EncryptionData.owned_accounts.append(websiteName); EncryptionDataInstance.saveArray()

	cwd = os.getcwd() #cwd + '\\id\\' + 
	connection = sqlite3.connect(websiteName + "keys" + ".db")
	cursor = connection.cursor()
	Store_keys = """CREATE TABLE IF NOT EXISTS
	keys(id PRIMARY KEY, key text)"""
	cursor.execute(Store_keys)
	cursor.execute("INSERT INTO keys VALUES (null, ?)", [key])
	connection.commit()
	#EncryptionDataInstance.owned_items.append(websiteName + "keys" + ".db")
	#EncryptionDataInstance.ItemsToEncrypt.append(websiteName + "keys" + ".db"); saveArray()

	params = (LoginUrl_encrypted, email_encrypted, password_encrypted)
	connection = sqlite3.connect(websiteName + ".db")
	cursor = connection.cursor()
	command1 = """CREATE TABLE IF NOT EXISTS
	websiteName(id PRIMARY KEY, LoginUrl text, email text, password text)"""
	cursor.execute(command1)
	cursor.execute("INSERT INTO websiteName VALUES (null, ?, ?, ?)", params)
	connection.commit()

	#loc = ('getcwd:      ', os.getcwd())					#\n = newline
	#print('__file__:    ', __file__)						#\t = tab
	#logf.write("%s"%n + "new account " + websiteName + " added" + '\n')
	#logf.close()
	def WriteButtonDefinitions():

		def WriteDynamicFunction(): # off/on switch logic for checkbox
			f = open("buttondefinitions.py", 'a')
			#f.write("websiteName" = websiteName)
			f.write('\n' + '\t' +"def " + websiteName + "(self, instance, value):" + '\n')
			f.write('\t' + '\t' + "if value is True:" + '\n')
			f.write('\t' + '\t' + '\t' + "#self.my_feedback_label.text = 'Hello, world!'" + '\n')
			#f.write('\t' + '\t' + '\t' + "#f = open(" + 'chromeHeader.py' + ", 'w+')" + '\n')
			#f.write('\t' + '\t' + '\t' + "f = open(" + "'" +  'chromeHeader.py' + "'" + ", 'a')" + '\n')
			#f.write('\t' + '\t' + '\t' + "loadaccount = " + "'" + "exec(open(" + '"' + websiteName + ".py" + '"' + ").read())" + "'" + '\n')
			#f.write('\t' + '\t' + '\t' + "f.write('\\n' + loadaccount + '\\n')" + '\n')
			#f.write('\t' + '\t' + '\t' + "f.close()" + '\n')
			f.write('\t' + '\t' + '\t' + "EncryptionDataInstance.dataInitialization()" + '\n')
			f.write('\t' + '\t' + '\t' + "EncryptionDataInstance.activeAccounts.append(" + "'" + websiteName + "')" + '\n')
			f.write('\t' + '\t' + '\t' + "EncryptionDataInstance.ItemsToDecrypt.append(" + "'" + websiteName + ".db'" + ")" + '\n')
			f.write('\t' + '\t' + '\t' + "EncryptionDataInstance.ItemsToDecrypt.append(" + "'" + websiteName + "keys.db'" + ")" + '\n')
			f.write('\t' + '\t' + '\t' + "EncryptionDataInstance.ItemsToDecrypt.append(" + "'" + websiteName + ".py'" + "); EncryptionDataInstance.saveArray();" + '\n')
			f.write('\t' + '\t' + '\t' + "EncryptionDataInstance.dataInitialization()" + '\n')
			f.write('\t' + '\t' + "else:" + '\n')
			f.write('\t' + '\t' + '\t' + "#self.my_feedback_label.text = 'Goodbye, world!'" + '\n')
			#f.write('\t' + '\t' + '\t' + "with open(" + "'" + "chromeHeader.py" + "'" + ", 'r') as f:" + '\n')
			#f.write('\t' + '\t' + '\t' + '\t' + "lines = f.readlines()" + '\n')
			#f.write('\t' + '\t' + '\t' + "with open(" + "'" + "chromeHeader.py" + "'" + ", 'w') as f:" + '\n')
			#f.write('\t' + '\t' + '\t' + '\t' + "for line in lines:" + '\n')
			#f.write('\t' + '\t' + '\t' + '\t' + '\t' + 'if line.strip(' + "'" + '\\n' + "'" + ") != " + '"' + "exec(open(" + "'" + websiteName + ".py" + "'" + ")" + ".read())" + '":' + '\n')
			#f.write('\t' + '\t' + '\t' + '\t' + '\t' + '\t' + "f.write(line)" + '\n')
			#f.write('\t' + '\t' + '\t' + "f.close()" + '\n')
			f.write('\t' + '\t' + '\t' + "EncryptionDataInstance.dataInitialization()" + '\n')
			f.write('\t' + '\t' + '\t' + "EncryptionDataInstance.activeAccounts.remove(" + "'" + websiteName + "')" + '\n')
			f.write('\t' + '\t' + '\t' + "EncryptionDataInstance.ItemsToDecrypt.remove(" + "'" + websiteName + ".db'" + ")" + '\n')
			f.write('\t' + '\t' + '\t' + "EncryptionDataInstance.ItemsToDecrypt.remove(" + "'" + websiteName + "keys.db'" + ")" + '\n')
			f.write('\t' + '\t' + '\t' + "EncryptionDataInstance.ItemsToDecrypt.remove(" + "'" + websiteName + ".py'" + ")" + '\n')
			f.write('\t' + '\t' + '\t' + "EncryptionDataInstance.saveArray();" + '\n')
			f.write('\t' + '\t' + '\t' + "EncryptionDataInstance.dataInitialization()" + '\n')
			f.close()
			#encrypt newly added files 
			#EncryptionDataInstance.ItemsToEncrypt.remove(websiteName + '.py')
			#EncryptionDataInstance.ItemsToEncrypt.remove(websiteName + 'keys.db')
			#EncryptionDataInstance.ItemsToEncrypt.remove(websiteName + '.db')
		#init file
		if os.path.exists('buttondefinitions.py'):
			print("writing function")
			WriteDynamicFunction()
		else:
			f = open("buttondefinitions.py", "w+")
			f = open("buttondefinitions.py", 'a')
			f.write("from encryptiondata import EncryptionData" + '\n')
			f.write("EncryptionDataInstance = EncryptionData()" + '\n')
			f.write("EncryptionDataInstance.dataInitialization()" + '\n')
			f.write("class functions():" + '\n')
			f.write('\t' + "def __init__(self, **kwargs):" + '\n')
			f.write('\t' + '\t' + "super(functions, self).__init__(**kwargs)" + '\n')
			f.write('\t' + "def dummyfunction():" + '\n')
			f.write('\t' + '\t' + "print('done')" + '\n')
			WriteDynamicFunction()
			f.close()
	WriteButtonDefinitions()

	def WriteButtons(): #kv declarative code for checkbox #https://stackoverflow.com/questions/26686631/how-do-you-scroll-a-gridlayout-inside-kivy-scrollview
		f = open("All.kv", 'a')#need write switch here to choose tab to write to
		f.write('\n')
		f.write('\t' + "CustLabel:" + '\n')
		f.write('\t' + '\t' "text: " + '"' + websiteName + '"' + '\n')
		f.write('\t' + '\t' "size_hint_x: " + ".80" + '\n')
		f.write('\t' + '\t' "font_size:30" + '\n')

		f.write('\t' + "CheckBox:" + '\n')
		f.write('\t' + '\t' "color:.294, .761, .623" + '\n')
		#f.write('\t' + '\t' + '\t' + '\t' "on_active: root.checkbox_click(self, self.active)" + '\n')
		f.write('\t' + '\t' "on_active: app." + websiteName + "(self, self.active)" + '\n') #root. changed to app.
		f.write('\t' + '\t' "size_hint_x: .80" + '\n')

		f.write('\t' + "CustLabel:" + '\n')
		f.write('\t' + '\t' "id: " + websiteName + "_feedback_label" + '\n')
		f.write('\t' + '\t' "text:" + '"' + "check to login" + '"' + '\n')
		f.write('\t' + '\t' "size_hintx: .80" + '\n')
		f.write('\t' + '\t' "font_size:30" + '\n')
		f.write('\n')		
		f.close()
	WriteButtons()

	#importlib.reload(webAccountButtons)
	#LoadwebAccountButtons()
	def Writescript(): #login scripts executed by chromeHeader #needs update
		f = open(websiteName + ".py", "w+")#create if not exist
		f = open(websiteName + ".py", "a+")
		f.write('import sqlite3' + '\n')
		f.write('import cryptography' + '\n')
		f.write('from cryptography.fernet import Fernet' + '\n')

		f.write("#import sqlite3" + '\n')
		f.write("#import cryptography" + '\n')
		f.write("#from cryptography.fernet import Fernet" + '\n')
		#f.write("def loadContents():" + '\n')
		f.write('class login():' + '\n')
		f.write('\t' + 'def __init__(self, **kwargs):' + '\n')
		f.write('\t' + '\t' + 'super(login, self).__init__(**kwargs)' + '\n')
		f.write('\t' + '\t' + 'def convertTuple(tup):' + '\n')
		f.write('\t' + '\t' + '\t' + "str = b''.join(tup)" + '\n')
		f.write('\t' + '\t' + '\t' + 'return(str)' + '\n')

		f.write('\t' + '\t' + "connection = sqlite3.connect(" + "'" + websiteName + "keys.db" + "')" + '\n')
		f.write('\t' + '\t' + "cursor = connection.cursor()" + '\n')
		f.write('\t' + '\t' + "cursor.execute(" + '"SELECT key FROM keys"' + ")" + '\n')
		f.write('\t' + '\t' + "results = cursor.fetchone()" + '\n')
		f.write('\t' + '\t' + "tup = results" + '\n')
		f.write('\t' + '\t' + "tuple = tup" + '\n')
		f.write('\t' + '\t' + "key = convertTuple(tup)" + '\n') 
		f.write('\t' + '\t' + "f = Fernet(key)" + '\n')
		
		f.write('\t' + '\t' + "connection = sqlite3.connect(" + "'" + websiteName + ".db" + "')" + '\n')
		f.write('\t' + '\t' + "cursor = connection.cursor()" + '\n')
		f.write('\t' + '\t' + "cursor.execute(" + '"SELECT LoginUrl FROM websiteName"' + ")" + '\n')
		f.write('\t' + '\t' + "results = cursor.fetchone()" + '\n')
		f.write('\t' + '\t' + "tup = results" + '\n')
		f.write('\t' + '\t' + "str = convertTuple(tup)" + '\n')
		f.write('\t' + '\t' + "decrypted = f.decrypt(str)" + '\n')
		f.write('\t' + '\t' + "login.url = decrypted.decode('utf-8')" + '\n')

		f.write('\t' + '\t' + "cursor.execute(" + '"SELECT email FROM websiteName"' + ")" + '\n')
		f.write('\t' + '\t' + "results = cursor.fetchone()" + '\n')
		f.write('\t' + '\t' + "tup = results" + '\n')
		f.write('\t' + '\t' + "tuple = tup" + '\n')
		f.write('\t' + '\t' + "str = convertTuple(tup)" + '\n')
		f.write('\t' + '\t' + "decrypted = f.decrypt(str)" + '\n')
		f.write('\t' + '\t' + "login.decoded_email = decrypted.decode('utf-8')" + '\n')

		f.write('\t' + '\t' + "cursor.execute(" + '"SELECT password FROM websiteName"' + ")" + '\n')
		f.write('\t' + '\t' + "results = cursor.fetchone()" + '\n')
		f.write('\t' + '\t' + "tup = results" + '\n')
		f.write('\t' + '\t' + "tuple = tup" + '\n')
		f.write('\t' + '\t' + "str = convertTuple(tup)" + '\n')
		f.write('\t' + '\t' + "decrypted = f.decrypt(str)" + '\n')
		f.write('\t' + '\t' + "login.decoded_password = decrypted.decode('utf-8')" + '\n')
		f.write('\t' + '\t' + "connection.close()" + '\n')

		#f.write("driver = webdriver.Chrome()" + '\n')
		#f.write("driver.get(decoded_url)" + '\n')
		#f.write("usernamebox = driver.find_element_by_id(" + "uid" + ")" + '\n')
		#f.write("Loginboxxpath = " + "'" + Loginboxxpath + "'" +'\n')
		#f.write("usernamebox = driver.find_element_by_xpath(Loginboxxpath)" + '\n')
		#f.write("usernamebox.clear()" + '\n')
		#f.write("usernamebox.send_keys(decoded_email)" + '\n')

		#f.write("passwordboxxpath = " + "'" + passwordboxxpath + "'" +'\n')
		#f.write("passwordbox = driver.find_element_by_xpath(passwordboxxpath)" + '\n')
		#f.write("passwordbox.clear()" + '\n')
		#f.write("passwordbox.send_keys(decoded_password)" + '\n')

		#f.write("Loginbuttonxpath = " + "'" + Loginbuttonxpath + "'" +'\n')
		#f.write("loginbutton = driver.find_element_by_xpath(Loginbuttonxpath).click()" + '\n')
		#f.write("passwordbox = driver.find_element_by_name(" + "pwd" + ")" + '\n')
		#f.write("passwordbox.clear()" + '\n')
		#f.write("passwordbox.send_keys(decoded_password)" + '\n')
		#f.write("#driver.find_element_by_name(" + "submitButton" + ").click()" + '\n')
		#f.write("driver.find_element_by_link_text(" + "Grumpy cats" + ").click()" + '\n')
		#f.write("loadContents()" + '\n')
		f.close()
		EncryptionDataInstance = EncryptionData()
		EncryptionDataInstance.dataInitialization()
		EncryptionDataInstance.owned_items.append(websiteName + "keys.db")
		EncryptionDataInstance.owned_items.append(websiteName + ".db")
		EncryptionDataInstance.owned_items.append(websiteName + ".py")
		EncryptionDataInstance.ItemsToEncrypt.append(websiteName + '.py')
		EncryptionDataInstance.ItemsToEncrypt.append(websiteName + 'keys.db')
		EncryptionDataInstance.ItemsToEncrypt.append(websiteName + '.db')
		EncryptionDataInstance.owned_accounts.append(websiteName)
		EncryptionDataInstance.saveArray()
		EncryptionInstance = encryptobj()
		EncryptionInstance.encryptor()
		#importlib.reload(checkbuttons)
		print('done, restart to load')
	Writescript()
	#restart or reload to load new buttons
	#importlib.reload("buttondefinitions.py")
	#importlib.reload("DigiLockApp.kv")
	#def restart():
	#	exec("restarter.py")
	#	exit()
	#restart()
	#importlib.reload(chromeHeader)

class DigiLockApp(App):
    def build(self):
        pass
        sm = ScreenManagement(transition=FadeTransition())
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(AccountsScreenApp(name='Accounts'))
        sm.add_widget(BrowserSelectionScreen(name='BrowserSelectionScreen'))
        sm.add_widget(AccountsScreenApp(name='AppAccounts'))
        #return Builder.load_file('accountsscreen.kv')
        #sm.add_widget(ActionsScreen(name='actions'))
        #sm.add_widget(LoginWindow(name='login'))
        #sm.add_widget(RegisterWindow(name='register'))
        # setting up window background color 
        #Window.clearcolor = (0, 0, .30, .60)
        return sm
if __name__ == '__main__':
    DigiLockApp().run() 
# Run the app
#if __name__ == '__main__': 
#    CheckBox().run()
#'\t' + 
#f.write("" + '\n')
#f.write("" + '\n')
#C:\Users\xjust\Desktop\DEV\OPS\DigiLock\DigiLockv3.1\kivyFolderExplorer\Main\mainv2.6\MultipleKV\multiplekv4