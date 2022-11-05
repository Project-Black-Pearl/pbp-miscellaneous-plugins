import requests
import time
from bs4 import BeautifulSoup


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
		time.sleep(1)
		entry = "title:", title, "link:", link
		results.append(entry)
		
	return(results)
	
	# ~ if search in title:
		# ~ for i in range(0, len(titles)):
			# ~ try:
				# ~ results.append(titles[i].text)
				# ~ results.append(link[i].attrs['href'])
			# ~ except:
				# ~ pass
	# ~ if results == []:
		# ~ results.append("Crackhub: Nothing Found")

	# ~ full = results[1::2]
	# ~ return(link)



# ~ usage:
print(crackhubSearch("hades"))
