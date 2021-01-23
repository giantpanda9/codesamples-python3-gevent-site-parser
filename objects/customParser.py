import lxml.html

class parser:
	def __init__(self):
		pass

	def getElementAttribute(self,pageText,value,attributeID):
		HTMLDocument = lxml.html.document_fromstring(pageText)
		HTMLElement = HTMLDocument.xpath(value)
		if (len(HTMLElement) >=1): 
			return HTMLElement[0].attrib[attributeID]
		return ""
	
	def parseAllLinks(self,pageText,domain):
		HTMLDocument = lxml.html.document_fromstring(pageText)
		HTMLElements = HTMLDocument.xpath("//a")
		returned = []
		if (len(HTMLElements) > 0):
			for HTMLElement in HTMLElements:
				if ("mailto:" in HTMLElement.attrib["href"] or HTMLElement.attrib["href"] == "" or HTMLElement.attrib["href"] == "javascript:void(0)"):
					continue 
				if ("http://" in HTMLElement.attrib["href"] or "https://" in HTMLElement.attrib["href"]): #absolute links
					if (domain in HTMLElement.attrib["href"]): # should contain only domain news.ycombinator.com
						returned.append(HTMLElement.attrib["href"])
				else: # relative links should all lead to news.ycombinator.com, but need to fix them
					returned.append("https://" + domain + "/" + HTMLElement.attrib["href"])
		return returned
	
