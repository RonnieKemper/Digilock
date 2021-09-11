#from DigiLock import kdffunction

#from refactor import EncryptionData
from encryptiondata import EncryptionData
EncryptionDataInstance = EncryptionData()
EncryptionDataInstance.dataInitialization()


class functions(EncryptionData):
	def __init__(self, **kwargs):
		super(functions, self).__init__(**kwargs)
		#mydata(getItemsToDecrypt())
		#buttondefinitions.mydata()
	def dummyfunction():
		print('dummyfunction')
	#def getItemsToDecrypt():
		#connection = sqlite3.connect("OwnedObjects.db")
		#cursor = connection.cursor()
		#cursor.execute("SELECT ItemsToDecrypt FROM OwnedObjects")
		#results = cursor.fetchall()
		#results = str(results)
		#results = results[3:-4]
		#del ItemsToDecrypt
		#ItemsToDecrypt = json.loads(results)
		#connection.close()
		#return ItemsToDecrypt
	def githubMain(self, instance, value): #, getItemsToDecrypt
		#global EncryptionDataInstance
		#global owned_items, ItemsToEncrypt, ItemsToDecrypt
		#EncryptionDataInstance = EncryptionData()
		#EncryptionDataInstance.dataInitialization()
		if value is True:
			#self.my_feedback_label.text = 'Hello, world!'
			#f = open('chromeHeader.py', 'w+')
			#getArray()
			#original = open('Account_imports.py').read()
			#f = open('Account_imports.py', 'a')
			#loadaccount = "exec(open('githubMain.py').read())"
			#loadaccount = "import githubMain"
			#newTab = "driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')"
			#login = "login()"
			#f.write('\n' + loadaccount + '\n' + original)
			#f.close()
			#get_value_to_decrypt = exec(open("value_to_decrypt.py").read())
			#f = open("value_to_encrypt.py", "r")
			#getItemsToDecrypt()
			#print(mydata)
			#print(functions)
			#activeAccounts = []
			#EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.append("githubMain"); print('active accounts:'); print(EncryptionDataInstance.activeAccounts)
			EncryptionDataInstance.ItemsToDecrypt.append("githubMain.db")
			EncryptionDataInstance.ItemsToDecrypt.append("githubMainkeys.db")
			EncryptionDataInstance.ItemsToDecrypt.append("githubMain.py"); EncryptionDataInstance.saveArray() #EncryptionDataInstance.saveItemsToDecrypt(); EncryptionDataInstance.saveactiveAccounts() #decrypt() <-login button
			#EncryptionDataInstance.dataInitialization()
			print(EncryptionDataInstance.activeAccounts)
		else:
			#self.my_feedback_label.text = 'Goodbye, world!'
			#with open('Account_imports.py', 'r') as f:
			#	lines = f.readlines()
			#with open('Account_imports.py', 'w') as f:
			#	for line in lines:
			#		#if line.strip('\n') != "exec(open('githubMain.py').read())":
			#		if line.strip('\n') != "import githubMain":
			#			f.write(line)
			#f.close()
			#get_value_to_encrypt = exec(open("value_to_encrypt.py").read())
			#f = open("value_to_encrypt.py", "w")
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.remove("githubMain")
			EncryptionDataInstance.ItemsToDecrypt.remove("githubMain.py")
			EncryptionDataInstance.ItemsToDecrypt.remove("githubMain.db")
			EncryptionDataInstance.ItemsToDecrypt.remove("githubMainkeys.db")
			#EncryptionDataInstance.ItemsToEncrypt.append("githubMain.py"); 
			EncryptionDataInstance.saveArray(); #encrypt() <-loginbutton
			#EncryptionDataInstance.dataInitialization()
	def stackexchange(self, instance, value): #, getItemsToDecrypt
		#global EncryptionDataInstance
		#global owned_items, ItemsToEncrypt, ItemsToDecrypt
		#EncryptionDataInstance = EncryptionData()
		#EncryptionDataInstance.dataInitialization()
		if value is True:
			#self.my_feedback_label.text = 'Hello, world!'
			#f = open('chromeHeader.py', 'w+')
			#getArray()
			#f = open('chromeHeader.py', 'a')
			#loadaccount = "exec(open('stackexchange.py').read())"
			#f.write('\n' + loadaccount + '\n')
			#f.close()
			#get_value_to_decrypt = exec(open("value_to_decrypt.py").read())
			#f = open("value_to_encrypt.py", "r")
			#getItemsToDecrypt()
			#print(mydata)
			#print(functions)
			#print('appending stackexchange to list')
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.append("stackexchange")
			EncryptionDataInstance.ItemsToDecrypt.append("stackexchange.py"); 
			EncryptionDataInstance.ItemsToDecrypt.append("stackexchange.db")
			EncryptionDataInstance.ItemsToDecrypt.append("stackexchangekeys.db")
			#print('saving list')
			EncryptionDataInstance.saveArray(); #decrypt() <-login button
			EncryptionDataInstance.dataInitialization()
		else:
			#self.my_feedback_label.text = 'Goodbye, world!'
			#with open('chromeHeader.py', 'r') as f:
			#	lines = f.readlines()
			#with open('chromeHeader.py', 'w') as f:
			#	for line in lines:
			#		if line.strip('\n') != "exec(open('stackexchange.py').read())":
			#			f.write(line)
			#f.close()
			#get_value_to_encrypt = exec(open("value_to_encrypt.py").read())
			#f = open("value_to_encrypt.py", "w")
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.remove("stackexchange")
			EncryptionDataInstance.ItemsToDecrypt.remove("stackexchange.py")
			EncryptionDataInstance.ItemsToDecrypt.remove('stackexchange.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('stackexchangekeys.db')
			#EncryptionDataInstance.ItemsToEncrypt.append("stackexchange.py"); 
			EncryptionDataInstance.saveArray(); #encrypt() <-loginbutton
			EncryptionDataInstance.dataInitialization()

	def facebook(self, instance, value):
		if value is True:
			#self.my_feedback_label.text = 'Hello, world!'
			#f = open(chromeHeader.py, 'w+')
			#f = open('chromeHeader.py', 'a')
			#loadaccount = 'exec(open("facebook.py").read())'
			#f.write('\n' + loadaccount + '\n')
			#f.close()
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.append("facebook")
			EncryptionDataInstance.ItemsToDecrypt.append('facebook.db')
			EncryptionDataInstance.ItemsToDecrypt.append('facebookkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.append('facebook.py'); EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
		else:
			#self.my_feedback_label.text = 'Goodbye, world!'
			#with open('chromeHeader.py', 'r') as f:
			#	lines = f.readlines()
			#with open('chromeHeader.py', 'w') as f:
			#	for line in lines:
			#		if line.strip('\n') != "exec(open('facebook.py').read())":
			#			f.write(line)
			#f.close()
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.remove("facebook")
			EncryptionDataInstance.ItemsToDecrypt.remove('facebook.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('facebookkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('facebook.py')
			EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
	def LinkedIn(self, instance, value):
		if value is True:
			#self.my_feedback_label.text = 'Hello, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.append('LinkedIn')
			EncryptionDataInstance.ItemsToDecrypt.append('LinkedIn.db')
			EncryptionDataInstance.ItemsToDecrypt.append('LinkedInkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.append('LinkedIn.py'); EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
		else:
			#self.my_feedback_label.text = 'Goodbye, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.remove('LinkedIn')
			EncryptionDataInstance.ItemsToDecrypt.remove('LinkedIn.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('LinkedInkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('LinkedIn.py')
			EncryptionDataInstance.saveArray();
	def FreeLancer(self, instance, value):
		if value is True:
			#self.my_feedback_label.text = 'Hello, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.append('FreeLancer')
			EncryptionDataInstance.ItemsToDecrypt.append('FreeLancer.db')
			EncryptionDataInstance.ItemsToDecrypt.append('FreeLancerkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.append('FreeLancer.py'); EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
		else:
			#self.my_feedback_label.text = 'Goodbye, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.remove('FreeLancer')
			EncryptionDataInstance.ItemsToDecrypt.remove('FreeLancer.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('FreeLancerkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('FreeLancer.py')
			EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
	def Reddit(self, instance, value):
		if value is True:
			#self.my_feedback_label.text = 'Hello, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.append('Reddit')
			EncryptionDataInstance.ItemsToDecrypt.append('Reddit.db')
			EncryptionDataInstance.ItemsToDecrypt.append('Redditkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.append('Reddit.py'); EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
		else:
			#self.my_feedback_label.text = 'Goodbye, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.remove('Reddit')
			EncryptionDataInstance.ItemsToDecrypt.remove('Reddit.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('Redditkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('Reddit.py')
			EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
	def Discord(self, instance, value):
		if value is True:
			#self.my_feedback_label.text = 'Hello, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.append('Discord')
			EncryptionDataInstance.ItemsToDecrypt.append('Discord.db')
			EncryptionDataInstance.ItemsToDecrypt.append('Discordkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.append('Discord.py'); EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
		else:
			#self.my_feedback_label.text = 'Goodbye, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.remove('Discord')
			EncryptionDataInstance.ItemsToDecrypt.remove('Discord.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('Discordkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('Discord.py')
			EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
	def Discord(self, instance, value):
		if value is True:
			#self.my_feedback_label.text = 'Hello, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.append('Discord')
			EncryptionDataInstance.ItemsToDecrypt.append('Discord.db')
			EncryptionDataInstance.ItemsToDecrypt.append('Discordkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.append('Discord.py'); EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
		else:
			#self.my_feedback_label.text = 'Goodbye, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.remove('Discord')
			EncryptionDataInstance.ItemsToDecrypt.remove('Discord.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('Discordkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('Discord.py')
			EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
	def BugCrowd(self, instance, value):
		if value is True:
			#self.my_feedback_label.text = 'Hello, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.append('BugCrowd')
			EncryptionDataInstance.ItemsToDecrypt.append('BugCrowd.db')
			EncryptionDataInstance.ItemsToDecrypt.append('BugCrowdkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.append('BugCrowd.py'); EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
		else:
			#self.my_feedback_label.text = 'Goodbye, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.remove('BugCrowd')
			EncryptionDataInstance.ItemsToDecrypt.remove('BugCrowd.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('BugCrowdkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('BugCrowd.py')
			EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
	def Fiver(self, instance, value):
		if value is True:
			#self.my_feedback_label.text = 'Hello, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.append('Fiver')
			EncryptionDataInstance.ItemsToDecrypt.append('Fiver.db')
			EncryptionDataInstance.ItemsToDecrypt.append('Fiverkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.append('Fiver.py'); EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
		else:
			#self.my_feedback_label.text = 'Goodbye, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.remove('Fiver')
			EncryptionDataInstance.ItemsToDecrypt.remove('Fiver.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('Fiverkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('Fiver.py')
			EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()

	def codegym(self, instance, value):
		if value is True:
			#self.my_feedback_label.text = 'Hello, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.append('codegym')
			EncryptionDataInstance.ItemsToDecrypt.append('codegym.db')
			EncryptionDataInstance.ItemsToDecrypt.append('codegymkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.append('codegym.py'); EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
		else:
			#self.my_feedback_label.text = 'Goodbye, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.remove('codegym')
			EncryptionDataInstance.ItemsToDecrypt.remove('codegym.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('codegymkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('codegym.py')
			EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()

	def bugcrowd(self, instance, value):
		if value is True:
			#self.my_feedback_label.text = 'Hello, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.append('bugcrowd')
			EncryptionDataInstance.ItemsToDecrypt.append('bugcrowd.db')
			EncryptionDataInstance.ItemsToDecrypt.append('bugcrowdkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.append('bugcrowd.py'); EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
		else:
			#self.my_feedback_label.text = 'Goodbye, world!'
			EncryptionDataInstance.dataInitialization()
			EncryptionDataInstance.activeAccounts.remove('bugcrowd')
			EncryptionDataInstance.ItemsToDecrypt.remove('bugcrowd.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('bugcrowdkeys.db')
			EncryptionDataInstance.ItemsToDecrypt.remove('bugcrowd.py')
			EncryptionDataInstance.saveArray();
			EncryptionDataInstance.dataInitialization()
