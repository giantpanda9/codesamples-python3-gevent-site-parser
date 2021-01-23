from objects.anyPage import anyPage
from objects.customParser import parser
from os.path import dirname, abspath
from configparser import ConfigParser
import json

class configurator:
	def __init__(self,value):
			configParser = ConfigParser()
			self._configPath = dirname(dirname(abspath(__file__))) + "/config/config.ini"
			configParser.read(self._configPath)
			self._config = configParser
			if (not self._config.has_section(value)):
				print(f"No page defined for {value}")
				supportedSections = config.sections()[1:]
				print(f"Page config could be defined for {supportedSections}")
				return 
			self._domain = self._config.get('global','domain')
			self._proxies = json.loads(self._config.get('global','proxyList'))
			self._proxyAllowed = self._config.get('global','proxyAllowed')
			self._startPage = self._config.get(value,'start')
			self._link = self._config.get(value,'link')
			self._clicksAllowed = self._config.get(value,'clicksAllowed')
			self._parserObject = parser()
			self._siteSection = value

	def _getMoreValue(self,pageNo):
		returned = []
		domain = self._domain
		proxies = self._proxies
		proxyAllowed = self._proxyAllowed
		startPage = self._startPage 
		link = self._link
		page = anyPage(domain,startPage,link, proxies,proxyAllowed)
		page.startOnly(0)
		page.setPageNo(pageNo)
		pageURL = page.getURL()
		
		parsePage = self._parserObject
		moreButton = parsePage.getElementAttribute(page.getData(),"//a[@class='morelink']","href")
		
		moreButtonId = moreButton.split("?")[1].split("=")[1]
		
		print(f"__Obtained pageid value {moreButtonId}")
		
		return moreButtonId
	
		
	def generateConfigList(self):
		returned = []
		domain = self._domain
		startPage = self._startPage 
		link = self._link
		proxies = self._proxies
		proxyAllowed = self._proxyAllowed
		page = anyPage(domain,startPage,link, proxies,proxyAllowed)
		page.startOnly(1)
		pageURL = page.getURL()
		siteSection = self._siteSection
		parsePage = self._parserObject
		print(f"_Setting up start page value for {siteSection}")
		if (siteSection == "main"): # exception if site section is main 
			startPageId = "1" # value is 1
		else: #others have first value stored on corresponding pages
			startPageId = parsePage.getElementAttribute(page.getData(),"//tr[@class='athing']","id")
		self._config[siteSection]["startPage"] = startPageId
		moreLink = startPageId # To be used later
		returned.append(startPageId)
		print(f"_Start page value for {siteSection} has been set as {startPageId}")

		clicksCount = self._clicksAllowed
		for moreButtonClick in range(1,int(clicksCount)+1):
			moreLink = self._getMoreValue(moreLink)
			returned.append(moreLink)		
		self._config[siteSection]["pagesList"] = json.dumps(returned)
		with open(self._configPath, 'w') as configfile:
			self._config.write(configfile)
			configfile.close()
