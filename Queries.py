import requests

URL = "https://api.iextrading.com/1.0"

r = requests.get(url = URL + "/stock/aapl/news/last/1")

data = r.json()

newUrl = data['url'][0]

print(newsUrl)

