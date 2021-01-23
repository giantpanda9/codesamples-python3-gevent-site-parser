from objects.anyPage import anyPage
from objects.customParser import parser
from os.path import dirname, abspath
from configparser import ConfigParser
import json

import gevent.monkey
gevent.monkey.patch_socket()
import gevent
from gevent import Greenlet

from datetime import datetime

class crawler:
	def __init__(self,value,viewresults,storeresults):
			configParser = ConfigParser()
			configPath = dirname(dirname(abspath(__file__))) + "/config/config.ini"
			configParser.read(configPath)
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
			self._pagesList = json.loads(self._config.get(value,'pageslist'))
			self._parserObject = parser()
			self._siteSection = value
			self._currentTimestamp = datetime.now()
			self._outputPath = dirname(dirname(abspath(__file__))) + "/output/"
			self._viewresults = viewresults
			self._storeresults = storeresults
			
	def _parsePage(self,pageNo):
		returned = []
		domain = self._domain
		proxies = self._proxies
		proxyAllowed = self._proxyAllowed
		startPage = self._startPage 
		link = self._link
		pagesList = self._pagesList
		page = anyPage(domain,startPage,link, proxies,proxyAllowed)
		page.startOnly(0)
		page.setPageNo(pagesList[pageNo])
		pageURL = page.getURL()
		
		print("Crawling " + pageURL)

		links = self._parserObject.parseAllLinks(page.getData(),domain)
		return links
	
	def _debugView(self,value,parsedList):
		domain = self._domain
		print(f"Links for {value} of the {domain} are below:")
		linksCount = 0
		for row in parsedList:
			linksCount = linksCount + 1
			print(f"{linksCount}. {row}")
	
	def _saveOutput(self,value,parsedList):
		runtimeTimestamp = self._currentTimestamp.strftime("%Y-%m-%d_%H:%M:%S")
		domain = self._domain
		outputPath = self._outputPath
		outputFilename = f"{outputPath}/{domain}_{value}_{runtimeTimestamp}_output.json"
		with open(outputFilename, 'w') as outputfile:
			outputfile.write(json.dumps(parsedList))
			outputfile.close()
		print(f"Results stored into {outputFilename}")
		
	def crawl(self):
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
		viewresults = self._viewresults 
		storeresults = self._storeresults  
		# starting clicking more button in gevent based on allowed clicks value in order not to hammer the site with requests
		clicksCount = self._clicksAllowed
		moreButtonClicks = [Greenlet.spawn(self._parsePage, i) for i in range(0, int(clicksCount) + 1)] # plus 1 for first page
		gevent.joinall(moreButtonClicks) # wating for all processes to finish
		for moreButtonClick in moreButtonClicks: # loop through results
			for parsedLink in moreButtonClick.value: # loop through results
				returned.append(parsedLink) # append actual link
		returned = list(set(returned))
		if (viewresults):
			self._debugView(siteSection,returned)
		if (storeresults):
			self._saveOutput(siteSection,returned)
