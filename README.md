# 🌐 TrendMap - AI Global News & Sentiment Analyzer

TrendMap adalah dashboard analitik pintar yang memanfaatkan **NewsAPI** dan **Google Gemini AI** untuk membaca, menganalisis, dan menyimpulkan sentimen berita global secara *real-time*.

Proyek ini dibuat sebagai **Final Project Hacktiv8**.

## 🚀 Fitur Utama
* **Pencarian Berita Dinamis:** Menarik berita berdasarkan topik, negara, atau nama perusahaan.
* **Analisis Sentimen AI:** Membaca konteks teks berita dan memberikan skor sentimen (0-100).
* **Gauge Chart Interaktif:** Visualisasi meteran sentimen yang responsif menggunakan Plotly.

## 🛠️ Teknologi yang Digunakan
* Python 3
* Streamlit (Web UI)
* Google GenAI (Gemini)
* NewsAPI
* Plotly (Visualisasi)

## ⚙️ Cara Menjalankan Aplikasi
1. Clone repositori ini.
2. Install dependencies: `pip install -r requirements.txt`
3. Buat file `.env` dan masukkan API Key:
   ```text
   NEWS_API_KEY=kunci_news_api_kamu
   GEMINI_API_KEY=kunci_gemini_api_kamu
Kemudian jalankan aplikasi: `streamlit run app.py`