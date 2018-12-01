import requests
from bs4 import BeautifulSoup


URL = "https://api.iextrading.com/1.0"

r = requests.get(url = URL + "/stock/market/news/last/1")

data = r.json( )

links = []

for elements in data:
    links.append(elements['url'])

print(links)


text = []

for link in links:
    r = requests.get(link)
    html = BeautifulSoup(r.text, 'html.parser')
    text.append(html.find_all('p'))

print(text)

