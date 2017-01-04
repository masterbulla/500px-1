import requests
from bs4 import BeautifulSoup

def download(url, filename):
	dl = requests.get(url, stream=True)
	with open(filename, 'wb') as f:
		for chunk in dl.iter_content():
			f.write(chunk)  # writes chunks to file
	print("Done.")


url=input("URL: ")
filename=input("File Name: ") + ".jpg"
raw = requests.get(url) #make a request to the URL
soup=BeautifulSoup(raw.text,'html.parser') #get the HTML

links= soup.find(property="og:image") #find meta with property=og:image
image=links.get('content') #get its content
if image != '':
	download(image, filename)