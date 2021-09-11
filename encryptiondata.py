import os
import sqlite3
import json

class EncryptionData(): #functions
	def __init__(self, **kwargs):
		super(EncryptionData, self).__init__(**kwargs)
		EncryptionData.owned_items = ['DigiLock.py', 'encryptiondata.py', 'chromeHeader.py']
		EncryptionData.ItemsToEncrypt = []
		EncryptionData.ItemsToDecrypt = []
		EncryptionData.owned_accounts = []
		EncryptionData.activeAccounts = []
	#https://stackoverflow.com/questions/18884782/typeerror-worker-takes-0-positional-arguments-but-1-was-given
	@staticmethod
	def getOwnedObjects():
		connection = sqlite3.connect("OwnedObjects.db")
		cursor = connection.cursor()
		cursor.execute("SELECT owned_items FROM OwnedObjects")
		results = cursor.fetchall()
		if results == '[]':
			pass
		else:
			try:
				results = str(results); #print(results)
				results = results[3:-4]; #print(results)
				owned_items = json.loads(results)
				EncryptionData.owned_items = owned_items
				connection.close(); 
				return owned_items
			except:
				print('oi err')
				pass
		#print(owned_items)
		
	'''
	@staticmethod
	def isENCRYPTED():
		connection = sqlite3.connect("OwnedObjects.db")
		cursor = connection.cursor()
		cursor.execute("SELECT ItemsToEncrypt FROM OwnedObjects")
		results = cursor.fetchall()
		results = str(results)
		results = results[3:-4] #bad practice lol sorry
		#del ItemsToEncrypt
		ItemsToEncrypt = json.loads(results)
		connection.close()
		#print(ItemsToEncrypt)
		EncryptionData.ItemsToEncrypt = ItemsToEncrypt
		return ItemsToEncrypt
	'''
	@staticmethod
	def getItemsToEncrypt():
		connection = sqlite3.connect("OwnedObjects.db")
		cursor = connection.cursor()
		cursor.execute("SELECT ItemsToEncrypt FROM OwnedObjects")
		results = cursor.fetchall(); #print(results)
		if results == '[]':
			pass
		else:
			try:		
				results = str(results); #print(results)
				results = results[3:-4]; #print(results)
				#del ItemsToEncrypt
				ItemsToEncrypt = json.loads(results)
				connection.close()
				print(ItemsToEncrypt)
				EncryptionData.ItemsToEncrypt = ItemsToEncrypt
				print(EncryptionData.ItemsToEncrypt)
				return ItemsToEncrypt
			except:
				print('ite err')
				pass

	@staticmethod
	def getItemsToDecrypt():
		connection = sqlite3.connect("OwnedObjects.db")
		cursor = connection.cursor()
		cursor.execute("SELECT ItemsToDecrypt FROM OwnedObjects")
		results = cursor.fetchall()
		if results == '[]':
			pass
		else:
			try:	
				results = str(results)
				results = results[3:-4]
				#del ItemsToDecrypt
				ItemsToDecrypt = json.loads(results)
				connection.close()
				#print(ItemsToDecrypt)
				EncryptionData.ItemsToDecrypt = ItemsToDecrypt
				return ItemsToDecrypt
			except:
				print('itd err')
				pass

	@staticmethod
	def getowned_accounts():
		connection = sqlite3.connect("OwnedObjects.db")
		cursor = connection.cursor()
		#command1 = """CREATE TABLE IF NOT EXISTS
		#owned_accounts(id PRIMARY KEY, accounts text)"""
		#cursor.execute(command1)
		#dummyacc = ['lololol']
		#cursor.execute("INSERT INTO accounts VALUES (null, ?)", dummyacc)
		cursor.execute("SELECT owned_accounts FROM OwnedObjects")
		results = cursor.fetchall()
		if results == '[]':
			owned_accounts = []
			return owned_accounts
		else:
			try:
				results = str(results)
				results = results[3:-4]
				owned_accounts = json.loads(results)
				connection.close()
				print(owned_accounts)
				EncryptionData.owned_accounts = owned_accounts
				return owned_accounts
			except Exception as e:
				print(e)
				pass
	#@staticmethod
	#def getOwned_URLS():
	#	connection = sqlite
	
	#@staticmethod
	#def getTables():

	
	@staticmethod
	def getactiveAccounts(): #https://duckduckgo.com/?t=ffab&q=python%2C+how+to+see+the+positional+arguments+that+were+given&atb=v1-1&ia=web
		#try:
		connection = sqlite3.connect("OwnedObjects.db")
		cursor = connection.cursor()
		#command1 = """CREATE TABLE IF NOT EXISTS
		#activeAccounts(id PRIMARY KEY, accounts text)"""
		#cursor.execute(command1)
		cursor.execute("SELECT activeAccounts FROM OwnedObjects")
		results = cursor.fetchall()
		results = str(results); #print(results)
		strip = results[3:-4]; #print(activeAccounts); print(type(activeAccounts))
		
		#try:
		activeAccounts = json.loads(strip); #print(activeAccounts)
		#except:
		#	print('active accs error')
		#	pass
		connection.close()
		print("activeAccounts:"); print(activeAccounts)
		EncryptionData.activeAccounts = activeAccounts
		list(EncryptionData.activeAccounts)
		return activeAccounts
		#except:
		#	print('active accs error')
		#	pass

	
	def dataInitialization(instance): #instance
		if os.path.exists("OwnedObjects.db"): 
			EncryptionData.getOwnedObjects()
			#print(self.owned_items)
			EncryptionData.getItemsToEncrypt()
			EncryptionData.getItemsToDecrypt()
			EncryptionData.getowned_accounts()
			#EncryptionData.getactiveAccounts()
			#print(EncryptionData.ItemsToDecrypt)
		else:
			#print(EncryptionData.owned_items)
			EncryptionData.saveArray()
			EncryptionData.owned_objects = EncryptionDataInstance.getOwnedObjects()
			EncryptionData.ItemsToEncrypt = EncryptionDataInstance.getItemsToEncrypt()
			EncryptionData.ItemsToDecrypt = EncryptionDataInstance.getItemsToDecrypt()
			EncryptionData.owned_accounts = EncryptionDataInstance.getowned_accounts()
			#EncryptionData.activeAccounts = EncryptionDataInstance.getactiveAccounts()
			#print(ItemsToDecrypt)
	
	#@staticmethod
	def saveArray(instance): #instance
		#global owned_items, ItemsToEncrypt, ItemsToDecrypt
		#print(ItemsToDecrypt)
		#print(EncryptionDataInstance.owned_items)
		#owned_items = EncryptionDataInstance.owned_items
		if os.path.exists('OwnedObjects.db'): #future implementation of db redundancy
			try:			
				os.remove('OwnedObjects.db')
			except:
				print('cant remove db error')
				pass

		#delete duplicates from list to avoid corruption
		print('saveArray')
		owned_items = EncryptionData.owned_items; #print(owned_items)
		ItemsToEncrypt = EncryptionData.ItemsToEncrypt; #print(ItemsToEncrypt)
		ItemsToDecrypt = EncryptionData.ItemsToDecrypt; #print(ItemsToDecrypt)
		owned_accounts = EncryptionData.owned_accounts; #print(owned_accounts)
		activeAccounts = EncryptionData.activeAccounts; #print(activeAccounts)
		res = []; [res.append(x) for x in owned_items if x not in res]; owned_items = res; a = json.dumps(owned_items)
		res = []; [res.append(x) for x in ItemsToEncrypt if x not in res]; ItemsToEncrypt = res; b = json.dumps(ItemsToEncrypt)
		res = []; [res.append(x) for x in ItemsToDecrypt if x not in res]; ItemsToDecrypt = res; c = json.dumps(ItemsToDecrypt)
		res = []; [res.append(x) for x in owned_accounts if x not in res]; owned_accounts = res; d = json.dumps(owned_accounts)
		res = []; [res.append(x) for x in activeAccounts if x not in res]; activeAccounts = res; e = json.dumps(activeAccounts)
		#e = activeAccounts
		params = (a, b, c, d, e)
		connection = sqlite3.connect("OwnedObjects.db")
		cursor = connection.cursor()
		store_data = """CREATE TABLE IF NOT EXISTS
		"OwnedObjects"(id PRIMARY KEY, owned_items text, ItemsToEncrypt text, ItemsToDecrypt text, owned_accounts text, activeAccounts text)"""
		cursor.execute(store_data)
		cursor.execute("INSERT INTO OwnedObjects VALUES (null, ?, ?, ?, ?, ?)", params) #params
		connection.commit()
		connection.close()
	'''
	def saveItemsToDecrypt(instance):
		ItemsToDecrypt = EncryptionData.ItemsToDecrypt; print(ItemsToDecrypt)
		res = []; [res.append(x) for x in ItemsToDecrypt if x not in res]; ItemsToDecrypt = res; c = json.dumps(ItemsToDecrypt)
		connection = sqlite3.connect("OwnedObjects.db")
		cursor = connection.cursor()
		param = (c)
		cursor.execute('DELETE FROM OwnedObjects WHERE id=ItemsToDecrypt')
		cursor.execute("INSERT INTO OwnedObjects WHERE id=ItemsToDecrypt VALUES (null, ?)", param)
		connection.commit()
		connection.close()
	'''
	@staticmethod
	def clearactiveAccounts():
		activeAccounts = []
		#res = []; [res.append(x) for x in activeAccounts if x not in res]; activeAccounts = res; e = json.dumps(activeAccounts)
		connection = sqlite3.connect("OwnedObjects.db")
		cursor = connection.cursor()
		#param = (e)
		cursor.execute('DELETE FROM OwnedObjects WHERE id = activeAccounts')
		#cursor.execute("INSERT INTO OwnedObjects WHERE id=activeAccounts VALUES (null, ?)", param)
		connection.commit()
		connection.close()
	'''
	@staticmethod
	def SaveOwned_Accounts():
		connection = sqlite3.connect("OwnedObjects.db")
		cursor = connection.cursor()
		owned_accounts = EncryptionData.owned_accounts; print(owned_accounts)
		res = []; [res.append(x) for x in owned_accounts if x not in res]; owned_accounts = res; d = json.dumps(owned_accounts)
		params = d
		store_data = """CREATE TABLE IF NOT EXISTS
		"OwnedObjects"(id PRIMARY KEY, owned_items text, ItemsToEncrypt text, ItemsToDecrypt text, owned_accounts text, activeAccounts text)"""
		cursor.execute(store_data)
		cursor.execute("INSERT INTO owned_accounts VALUES (?)", params) #params
		connection.commit()
		connection.close()
	'''
	@staticmethod
	def HARDRESET():
		EncryptionDataInstance.dataInitialization()
		EncryptionData.ItemsToEncrypt = []
		EncryptionData.ItemsToDecrypt = []
		EncryptionData.owned_accounts = []
		EncryptionData.activeAccounts = []
		EncryptionDataInstance.saveArray()
'''	
EncryptionDataInstance = EncryptionData()
EncryptionDataInstance.dataInitialization()
EncryptionDataInstance.getOwnedObjects()
EncryptionDataInstance.getItemsToEncrypt()
EncryptionDataInstance.getItemsToDecrypt()
EncryptionDataInstance.getactiveAccounts()
EncryptionDataInstance.saveArray()
'''
