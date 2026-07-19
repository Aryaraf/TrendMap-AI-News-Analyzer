import requests
import os
from google.genai import Client 
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

topik = "technology asia"
url = f"https://newsapi.org/v2/everything?q={topik}&apiKey={NEWS_API_KEY}&language=en&pageSize=3"
response = requests.get(url)
data = response.json()

kumpulan_berita = ""
for i, artikel in enumerate(data['articles']):
    kumpulan_berita += f"{i+1}. Judul: {artikel['title']}\n"

print("--- BERITA YANG DIDAPAT ---")
print(kumpulan_berita)

print("Sedang menganalisis sentimen menggunakan Gemini... ⏳\n")

prompt = f"""
Kamu adalah seorang analis data ahli. Tolong baca daftar berita berikut:

{kumpulan_berita}

Tugasmu:
1. Berikan kesimpulan sentimen keseluruhan (POSITIF / NEGATIF / NETRAL) dari berita-berita di atas.
2. Berikan alasan singkat dalam 1-2 kalimat kenapa kamu memberikan penilaian tersebut.
"""

client = Client(api_key=GEMINI_API_KEY)

hasil = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt
)

print("--- HASIL ANALISIS AI ---")
print(hasil.text)