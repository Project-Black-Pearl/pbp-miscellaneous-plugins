import time
import requests
from bs4 import BeautifulSoup
import unidecode, json

def gameLinker(dl_link):
	startUrl = dl_link
	startReq = requests.get(startUrl)
	startSoup = BeautifulSoup(startReq.content, 'html.parser')
	contents = startSoup.find_all('div', class_='otfm-sp__content')
	
	linklist = [] 
	
	for content in contents:
		line = content.find('a')
		if line != None:
			link = line.get("href")
			if "steamstatic" not in link:
				linklist.append(link)
	return(linklist)

# ~ usage:
print(gameLinker("https://crackhub.site/stray-fitgirl-repack-kaos-repack-portable/#"))
