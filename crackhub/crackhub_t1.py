import requests
import time
from bs4 import BeautifulSoup
import unidecode, json


with open("crackhub-results.json",'w+') as file:
	base = '''{"response":[]	
}'''
	file.write(base)


def write_json(new_data, filename='crackhub-results.json'):
			with open(filename,'r+', encoding='utf-8') as file:
				file_data = json.load(file)
				file_data["response"].append(new_data)
				file.seek(0)
				json.dump(file_data, file, indent = 4)



# Search
def crackhubSearch(search):
	results = []

	url = "https://crackhub.site/?s="+search
	startReq = requests.get(url)
	startSoup = BeautifulSoup(startReq.content, 'html.parser')
	titles = startSoup.find_all('h2', class_='entry-title')
	
	for title in titles:
		link = title.find('a')
		link = link.get("href")
			
		title = title.text.strip()
		titleCheck = title.lower()
		searchCheck = search.lower()
		if searchCheck in titleCheck:
			time.sleep(1)
			entry = {"title": title,
						 "URIs": link
					}
				
			print(entry)
			write_json(entry)
			results.append(entry)

	
# ~ usage:
crackhubSearch("stray")
