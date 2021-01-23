import requests
import random

class anyPage:
	def __init__(self,domain,start,link,proxies,proxyAlowed):
			self._domain = domain
			self._startfrom = start
			self._workinglink = link
			self._startOnly = 0
			self._currentpage = 1 #Default value - must be changed
			self._proxy = {
				"https": random.choice(proxies)
			}
			self._proxyAlowed = proxyAlowed
			
	def setPageNo(self,value):
		self._currentpage = value
		
	def startOnly(self,value):
		if (value):
			self._startOnly = 1
		else:
			self._startOnly = 0

	def getURL(self):
		returned = ""
		domain = self._domain
		startPage = self._startfrom
		link = self._workinglink
		pageno = self._currentpage
		startOnlyFlag = self._startOnly
		if (startOnlyFlag): # if config flag set
			returned = f"https://{domain}/{startPage}" # get first page from any pagination method
		else:
			returned = f"https://{domain}/{startPage}{link}{pageno}" # otherwise use page with number		
		return returned

	def getData(self):
		pageURL = self.getURL();
		returned = ""
		if (pageURL == ""):
			return 0;
		proxyAllowed = self._proxyAlowed
		if (proxyAllowed == 1):
			response = requests.get(pageURL, proxies=self._proxy)
		else:
			response = requests.get(pageURL)
		
		if response.status_code == 200:
			returned = response.text
		
		return returned
