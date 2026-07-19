import requests

NEWS_API_KEY = "ca12fd888efe42ceacdb3db9d4231f75" 
topik = "technology asia"

url = f"https://newsapi.org/v2/everything?q={topik}&apiKey={NEWS_API_KEY}&language=en&pageSize=3"
response = requests.get(url)
data = response.json()

print("--- 3 NEWS UPDATE ---")
for artikel in data['articles']:
    print(f"Judul: {artikel['title']}")
    print(f"Sumber: {artikel['source']['name']}")
    print("-" * 20)