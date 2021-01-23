#!/usr/bin/env python

from optparse import OptionParser
from configparser import ConfigParser
from os.path import dirname, abspath
from objects.customCrawler import crawler
from objects.customCrawlerConfigurator import configurator

def configData():
	configInstance1 = configurator("main")
	configInstance1.generateConfigList()
	configInstance2 = configurator("comments")
	configInstance2.generateConfigList()
	return 1

def crawl(viewresults,storeresults):
	crawlerInstance1 = crawler("main",viewresults,storeresults)
	crawlerInstance1.crawl()
	crawlerInstance2 = crawler("comments",viewresults,storeresults)
	crawlerInstance2.crawl()
	return 1

def main():
	
	parser = OptionParser(usage="usage: %prog [options]", version="%prog 1.0")
	parser.add_option("-c", "--config",
						action="store_true",
						default=False,
						help="configure pages for crawler in a single thread mode - should be run on cron once in 2 or more days")
	parser.add_option("-r", "--crawl",
						action="store_true",
						default=False,
						help="crawl site in gevent mode",)
	parser.add_option("-v", "--view",
						action="store_true",
						default=False,
						help="view results on screen in crawl site in gevent mode",)
	parser.add_option("-s", "--store",
						action="store_true",
						default=False,
						help="store results into json output in crawl site in gevent mode",)
	(options, args) = parser.parse_args()
	if (options.config):
		configData()
	if (options.crawl):
		crawl(options.view,options.store)
	
if __name__=='__main__': main()
