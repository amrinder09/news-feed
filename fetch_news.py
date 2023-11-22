import requests

url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=524fc276c0884f309911cf483492c691"
response = requests.get(url)
data = response.json()

print(data)
