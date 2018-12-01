import requests
import ssl
import config

URL = "https://api.iextrading.com/1.0"

equitiesList = ["aapl", "googl", "fb", "msft", "gs", "ge"]

r = requests.get(url = URL + "/stock/aapl/news/last/5")
data = r.json()

for number in range(len(data)):
    config.queue.put(data[number]['url'])


