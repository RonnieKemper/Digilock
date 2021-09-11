from win32com.client import Dispatch
import selenium
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import requests
import platform
import sys
import zipfile
import os

#platform = platform.platform()
def CheckForDriverUpdate():
	print("checking for update...")
	try:
		driver = webdriver.Chrome()
		browserVersion = driver.capabilities['browserVersion']
		Driverversion = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
		print("browserVersion: " + browserVersion)
		print("Driver version: " + Driverversion)
		#print(str1[0:2])
		#print(str2[0:2])
		if browserVersion[0:2] != Driverversion[0:2]: 
			print("updating driver")
			update()
		else:
			print("versions are compatible")
			exit()
	except:
		print("error")
		update()
CheckForDriverUpdate()
def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"


def get_version_via_com(filename):
	parser = Dispatch("Scripting.FileSystemObject")
	try:
		version = parser.GetFileVersion(filename)
	except Exception:
		return None
	return version
def update():
	linux_distribution()
	system = platform.system()
	machine = platform.machine()
	platform = platform.platform()

	print("system: " + system)
	print("machine: " + machine)
	print("platform: " + platform)

	if system == 'Windows':
		page = "chromedriver_win32.zip"
		ext = "_win32.zip"


	if system == 'linux':
		page = "chromedriver_linux64.zip"
		ext = "_linux64.zip"

	if system == 'mac':
		page == "chromedriver_mac64.zip"
		ext = "_mac64.zip"

	if __name__ == "__main__":
		paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
				r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
		version = list(filter(None, [get_version_via_com(p) for p in paths]))[0]
		print("chromebrowser version: " + version)
		link = 'https://chromedriver.storage.googleapis.com/' + version + '/' + page
		print(link)
	try:
		os.remove('chromedriver.exe')
	except:
		pass
	# URL of the image to be downloaded is defined as image_url 
	r = requests.get(link) # create HTTP response object   
	# send a HTTP request to the server and save 
	# the HTTP response in a response object called r 
	with open("chromedriver" + ext,'wb') as f:   
	    # Saving received content as a png file in 
	    # binary format   
	    # write the contents of the response (r.content) 
	    # to a new file in binary mode. 
	    f.write(r.content) 

	with zipfile.ZipFile('chromedriver' + ext, 'r') as zip_ref:
	    zip_ref.extractall() #'chromedriver.exe'
	    try:
	    	os.remove('chromedriver' + ext)
	    except:
	    	pass
	exit()