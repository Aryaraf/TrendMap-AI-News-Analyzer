import streamlit as st
import requests
import os
from google.genai import Client
from dotenv import load_dotenv
import plotly.graph_objects as go

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="TrendMap", page_icon=":newspaper:", layout="wide")

st.markdown("""
    <style>
    .stButton>button { background-color: #0A66C2; color: white; border-radius: 8px; width: 100%; }
    .stButton>button:hover { background-color: #004182; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("🌐 TrendMap - AI Global News & Sentiment Analyzer")
st.markdown("Menganalisis setimen pasar secara *real-time* menggunakan Gemini AI.")
st.markdown("---")

col_kiri, col_kanan = st.columns([1, 2])

with col_kiri:
    st.subheader("🔍 Parameter Pencarian")
    topik = st.text_input("Masukkan Topik, Negara, atau Perusahaan:", "technology asia")
    jumlah_berita = st.slider("Jumlah berita yang dianalisis:", min_value=3, max_value=10, value=5)
    tombol_cari = st.button("Mulai Analisis Sentimen 🚀")

if tombol_cari:
    with st.spinner("Sedang menarik data berita dan menganalisis dengan AI... ⏳"):
        url = f"https://newsapi.org/v2/everything?q={topik}&apiKey={NEWS_API_KEY}&language=en&pageSize={jumlah_berita}"
        response = requests.get(url)
        data = response.json()

        if data.get('status') != 'ok' or len(data.get('articles', [])) == 0:
            st.error("Gagal mengambil berita atau tidak ada berita yang relevan ditemukan.")
        else:
            kumpulan_berita = ""
            for i, artikel in enumerate(data['articles']):
                kumpulan_berita += f"{i+1}. Judul: {artikel['title']}\n"
            
            prompt = f"""
            Kamu adalah analis data keuangan profesional. Baca {jumlah_berita} judul berita terbaru ini mengenai "{topik}":

            {kumpulan_berita}

            Tugasmu:
            1. Tentukan Skor Sentimen dari 0 (Sangat Negatif) sampai 100 (Sangat Positif). 50 adalah Netral.
            2. Berikan analisis singat 2-3 kalimat kenapa skornya demikian.

            PENTING! Format jawabnmu HARUS PERSIS seperti di bawah ini tanpa tambahan karakter/bintang/bold markdown:
            SKOR: [Angka]
            ANALISIS: [Penjelasanmu]
            """

            client = Client(api_key=GEMINI_API_KEY)
            hasil = client.models.generate_content(
                model='gemini-3.5-flash',
                contents=prompt
            )

            teks_hasil = hasil.text

            if "ANALISIS:" in teks_hasil:
                bagian = teks_hasil.split("ANALISIS:")
                skor_str = bagian[0].replace("SKOR:", "").strip()
                analisis_teks = bagian[1].strip()
                skor_angka = int(skor_str)
            else:
                skor_angka = 50
                analisis_teks = "teks_hasil"

            with col_kanan:
                st.subheader("📊 Dashboard Sentimen AI")

                fig = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = skor_angka,
                    title = {'text': f"Indeks Sentimen: {topik.upper()}"},
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    gauge = {
                        'axis': {'range': [0, 100]},
                        'bar': {'color': "#2C3E50"},
                        'steps' : [
                            {'range': [0, 40], 'color': "#FF9999"},
                            {'range': [40, 60], 'color': "#FFFF99"},
                            {'range': [60, 100], 'color': "#99FF99"}
                            ]
                    }
                ))
                st.plotly_chart(fig, use_container_width=True)

                st.info(f"**Kesimpulan AI:**\n\n{analisis_teks}")
                
        with col_kiri:
            st.markdown("### 📰 Sumber Berita yang Dianalisis")
            st.text(kumpulan_berita)