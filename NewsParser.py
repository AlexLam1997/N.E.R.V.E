import requests
r = requests.get("https://seekingalpha.com/news/3413708-microsoft-overtakes-apple-valuable-u-s-company")

print(r.text)